from translation import translate
from pydantic import BaseModel
import pickle
import sqlite3
import pandas as pd

def charger_model():
    model_path = r"/home/geoffroy/Projets/Rendus_Ecole_Simplon/PCO/E1/code/api/pipeline_logisticregression0.83f1.pkl"
    model = pickle.load(open(model_path, "rb"))
    return model

model = charger_model()

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
    dict_pred_fr = dict(input_data)

    # Traduction du dictionnaire en anglais pour la prédiction
    dict_pred_en = dict_pred_fr.copy()
    for key, value in dict_pred_en.items():
        value = translate(value)
        dict_pred_en[key] = value

    # Prédiction
    input_df = pd.DataFrame(dict_pred_en, index=[0])
    prediction = model.predict(input_df)[0]

    # Insertion des données en base sqlite
    # Complétion du dictionnaire avec le résultat
    if prediction == "Yes":
        id_reponse = 1
    elif prediction == "No":
        id_reponse = 2

    dict_pred_fr["id_reponse"] = id_reponse

    # Entrée du questionnaire complet en base
    conn = sqlite3.connect("/home/geoffroy/Projets/Rendus_Ecole_Simplon/PCO/E1/code/bdd_sqlite_predictions/predictions.db")
    cursor = conn.cursor()
    print(tuple(dict_pred_fr.keys()))
    request = f"""INSERT INTO questionnaire {tuple(dict_pred_fr.keys())}
    VALUES {tuple(dict_pred_fr.values())}"""
    cursor.execute(request)
    conn.commit()
    conn.close()

predict(dict_example)