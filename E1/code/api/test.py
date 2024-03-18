from translation import translate
from pydantic import BaseModel
import pickle
import sqlite3
import pandas as pd

dict_example = {
    "Age" : 25,
    "Gender" : "Homme",
    "self_employed" : "Oui",
    "family_history" : "Oui",
    "work_interfere" : "Souvent",
    "no_employees" : '1-5',
    "remote_work" : "Oui",
    "tech_company" : "Oui",
    "benefits" : "Oui",
    "care_options" : "Oui",
    "wellness_program" : "Oui",
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

def predict(input_data: Issick):
    print(type(input_data))
    print(input_data)

di = predict(dict_example)