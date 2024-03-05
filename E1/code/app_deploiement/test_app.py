from fastapi.testclient import TestClient
from app import app

input_data_dict = {"Age" : 35,
"Gender" : "Female",
"self_employed" : "Other",
"family_history" : "No",
"work_interfere" : "Not concerned",
"no_employees" : "More than 1000",
"remote_work" : "Yes", 
"tech_company" : "Yes",
"benefits" : "Yes", 
"care_options" : "Not sure", 
"wellness_program" : "No", 
"seek_help" : "Yes",
"anonymity" : "Yes", 
"leave" : "Somewhat easy", 
"mental_health_consequence" : "No",
"phys_health_consequence" : "No", 
"coworkers" : "Some of them", 
"supervisor" : "Yes",
"mental_health_interview" : "No", 
"phys_health_interview" : "Maybe",
"mental_vs_physical" : "Don't know", 
"obs_consequence" : "No"}

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200 
    assert response.json() == {"details" : "Hellooooooo  !"}


def test_prediction():
    response = client.post("/predict", json=input_data_dict)
    assert response.status_code == 200 
    assert response.json() == {"prediction": "No"}
