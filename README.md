# Notable-TakeHome-Assignment

This repository contains implementation of the Notable Take Home Assignment. <br>
Submitter - <br>
Himanshu Gupta (hgupta@umass.edu) <br>

# Prerequisite to run the code
Python = "3.8"
pipenv package (Can be installed using the command: pip install --user pipenv)

# Commands to activate the Virtual environment
1. Go to the source directory and locate the file `Pipfile`.
2. Run the command: `pipenv install`
3. Run the command `pipenv shell` to activate and enter the virtual environment.

# Steps to run the web server
1. Run the command `python main.py` to start the flask server. 
(The web server will run on the localhost(127.0.0.1) and port 5000)
2. One can use postman to test the APIs.

# API Documentation

## Get a list of all doctors
URL: `127.0.0.1/doctors`

Method: `GET`

URL Arguments: `NA` 

Payload Format: `NA`

## Add a new doctor
URL: `127.0.0.1/doctors`

Method: `POST`

URL Arguments: `NA` 

Payload Format: {'firstname': <doctor's first name>, 'lastname': <doctor's last name>}

(All the fields are required)

## Add appointments for a doctor
URL: `127.0.0.1/doctors/<doctor_id>/appointments`

Method: `POST`

URL Arguments: `NA` 

Payload Format:

{
    "patient_firstname": <patient's first name>,
    "patient_lastname": <patient's last name>,
    "appointment_date": <appointment date in format YYYY:MM:DD>
    "appointment_time": <appointment_time in format HH:MM>
}
    
(All the fields are required)

## Get appointments of a doctor on a particular date
URL: `127.0.0.1/doctors/<doctor_id>/appointments?date=<appointment_date>`
    
Method: `GET`
    
URL Arguments: `date` 
    
Payload Format: `NA`
    

## Delete existing appointments of a doctor
URL: `127.0.0.1/doctors/<doctor_id>/appointments/<appointment_id>
    
Method: `DELETE`
    
URL Arguments: `NA`
    
Payload Format: `NA`

# API Response Format

{
    
    "data": <Requested data>,
    
    "message": <Failure or Success message>,
    
    "status": <Failure or Success>,
    
    "validation_code": <Status Code>
    
}
    
## Run Automated test command: pytest tests/test_api.py
(Could only add 1 testcase as of now)
