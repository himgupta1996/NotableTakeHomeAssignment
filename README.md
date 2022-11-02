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
(The web server will run on the localhost(127.0.0.1) and port 80)
2. Go to the browser and hit the address `http://127.0.0.1:5000/` to enter the home of the web server.

# Steps to run tests:
1. Go to the source directory and locate the tests folder.
2. Run the command `pytest test_api.py` to start the tests and generate the test results report.
