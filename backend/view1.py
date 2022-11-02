from crypt import methods
from tracemalloc import start
from urllib import request
from flask import Blueprint, request, render_template, jsonify
from .models import Doctor, Appointment
import json
from . import db
from backend.Utils.response_util import get_failed_response, get_success_response
from backend.Utils.format_util import validate_date, validate_time
from datetime import datetime, timedelta
from flask_expects_json import expects_json

view1 = Blueprint('view1', __name__)

# Get a list of all doctors
# Add a new doctor
@view1.route('/doctors', methods = ["GET", "POST"])
def doctors():
    if request.method == "GET":
        try:
            query_doctors = Doctor.query.all()

            doctors = []

            for doc in query_doctors:
                doc_info = doc.__dict__
                del doc_info['_sa_instance_state']
                doctors.append(doc_info)

            return get_success_response(output=doctors)
        except Exception as e:
            return get_failed_response(message=str(e))

    if request.method == "POST":
        try:
            doc_data = json.loads(request.data)
            firstname = doc_data.get('firstname')
            lastname = doc_data.get('lastname')
            new_doc = Doctor(firstname = firstname, lastname = lastname)
            db.session.add(new_doc)
            db.session.commit()
            return get_success_response(output = {"id": new_doc.id}, message="Doctor added successfully")
        except Exception as e:
            return get_failed_response(message=str(e))

# Get existing appointments for a doctor
# Add a new appointment for a doctor
# Delete an existing appointment for a doctor
@view1.route('/doctors/<doctor_id>/appointments', methods = ["GET", "POST"])
@view1.route('/doctors/<doctor_id>/appointments/<appointment_id>', methods = ["DELETE"])
def doctor_appointments(doctor_id, appointment_id = None):
    if request.method == "GET":
        try:
            print(doctor_id) 
            appt_date = request.args.get("date")

            ## Check if the request has date in the argument
            if not appt_date:
                raise Exception("Argument Error: 'date' not present in the arguments.")

            ## Checking the format of the appt day string
            if not validate_date(appt_date):
                raise Exception("Argument Error: 'date' in incorrect format, should be YYYY:MM:DD")
            
            query_doctor_appointments = Appointment.query.filter_by(doctor_id = doctor_id, start_date = appt_date).all()
            doctor_appointments = []
            
            for appt in query_doctor_appointments:
                appt_info = appt.__dict__
                del appt_info['_sa_instance_state']
                doctor_appointments.append(appt_info)

            return get_success_response(output=doctor_appointments)
        except Exception as e:
            return get_failed_response(message=str(e))

    if request.method == "DELETE":
        try:
            query_doctor_appointment = Appointment.query.filter_by(doctor_id=doctor_id, id = appointment_id).one()
            print(query_doctor_appointment)
            if query_doctor_appointment:
                db.session.delete(query_doctor_appointment)
                db.session.commit()
                return get_success_response(message="Appointment deleted successfully")

        except Exception as e:
            return get_failed_response(message=str(e))
    
    if request.method == "POST":
        try:
            ## Check if the doctor id present in the System
            doc = Doctor.query.filter_by(id = doctor_id).one()

            if doc == None:
                raise Exception(f"Doctor with id '{doctor_id}' not present.")

            ## Get the data to be inserted
            appt_data = json.loads(request.data)
            patient_firstname = appt_data.get('patient_firstname')
            patient_lastname = appt_data.get('patient_lastname') 
            appt_date = appt_data.get('appointment_date') 
            appt_time = appt_data.get('appointment_time')
            kind = appt_data.get('kind')
            
            ## Checking the format of the appt time string
            if not validate_time(appt_time):
                raise Exception("Argument Error: 'time' in incorrect format, should be HH:MM and new appointments can only start at 15 minute intervals")

            ## Checking the format of the appt day string
            if not validate_date(appt_date):
                raise Exception("Argument Error: 'date' in incoect format, should be YYYY:MM:DD")

            ## Checking if the kind of the appointment is correct
            if kind != "New Patient" and kind != "Follow-up":
                raise Exception("'kind' value incorrect, can be either 'New Patient' or 'Follow-up'")
            
            ## Get existing appointments for the given time
            query_appointments = Appointment.query.filter_by(doctor_id=doctor_id, start_date = appt_date, start_time = appt_time).all()
            if len(query_appointments)>=3:
                raise Exception("No more appointment can be taken at this particular time for the doctor.")

            new_appt = Appointment(patient_firstname = patient_firstname, patient_lastname = patient_lastname, start_date = appt_date, start_time = appt_time, kind = kind, doctor = doc)
            db.session.add(new_appt)
            db.session.commit()

            return get_success_response(output = {"appointment_id": new_appt.id, "doctor_id": doc.id}, message="Appointment added successfully")

        except Exception as e:
            return get_failed_response(message=str(e))