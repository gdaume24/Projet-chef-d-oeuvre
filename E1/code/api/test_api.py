from fastapi.testclient import TestClient
from api import app

input_data_dict = {
    "Age" : 55,
    "Gender" : "Femme",
    "self_employed" : "Non",
    "family_history" : "Non",
    "work_interfere" : "Souvent",
    "no_employees" : '1-5',
    "remote_work" : "Non",
    "tech_company" : "Non",
    "benefits" : "Non",
    "care_options" : "Non",
    "wellness_program" : "Non",
    "seek_help" : "Oui",
    "anonymity" : "Oui",
    "leave" : "Très facilement",
    "mental_health_consequence" : "Oui",
    "phys_health_consequence" : "Oui",
    "coworkers" : "Oui",
    "supervisor" : "Oui",
    "mental_health_interview" : "Oui",
    "phys_health_interview" : "Oui",
    "mental_vs_physical" : "Oui",
    "obs_consequence" : "Oui"
}

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200 
    assert response.json() == {"details" : "Hellooooooo  !"}


def test_prediction():
    response = client.post("/predict", params={"input_data":input_data_dict})
    assert response.status_code == 200 
    assert response.json() == {"prediction": "Yes"}
