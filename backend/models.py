from pickle import FALSE
from . import db
from sqlalchemy.sql import func

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    appointments = db.relationship('Appointment', backref='doctor', lazy=True)

    def __repr__(self):
        return f'<Doctor {self.firstname} {self.lastname}>'

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable = False)
    patient_firstname = db.Column(db.String(100), nullable=False)
    patient_lastname = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.String(10))
    start_time = db.Column(db.String(10))
    kind = db.Column(db.String(10))
    def __repr__(self):
        return f'<Appointment {self.id}>'
