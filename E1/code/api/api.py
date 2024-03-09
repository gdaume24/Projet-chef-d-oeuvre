from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel
import pickle
import os


def charger_model():
    model_path = r"pipeline_logisticregression0.83f1.pkl"
    model = pickle.load(open(model_path, "rb"))
    return model

class Issick(BaseModel):
    Age : int
    Gender : str
    self_employed : str
    family_history : str
    work_interfere : str
    no_employees : str
    remote_work : str
    tech_company : str
    benefits : str
    care_options : str
    wellness_program : str
    seek_help : str
    anonymity : str
    leave : str
    mental_health_consequence : str
    phys_health_consequence : str
    coworkers : str
    supervisor : str
    mental_health_interview : str
    phys_health_interview : str
    mental_vs_physical : str
    obs_consequence : str


app = FastAPI()

model = charger_model()

@app.get("/")
def home():
    return {"details" : "Hellooooooo  !"}
 
@app.post("/predict")
def predict(input_data: Issick):
    input_data_dict = dict(input_data)
    input_df = pd.DataFrame(input_data_dict, index=[0])
    prediction = model.predict(input_df)[0]

    return {"prediction" : prediction}

