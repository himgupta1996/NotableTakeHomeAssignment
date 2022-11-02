import requests
import json

def test_add_doctor():
    response = requests.post('http://127.0.0.1:5000/doctors', json = {"firstname": "Himanshu","lastname": "Gupta"})
    print(response.status_code)
    assert response.status_code == 200