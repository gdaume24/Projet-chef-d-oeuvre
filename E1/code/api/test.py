from translation import translate
from pydantic import BaseModel
import pickle
import sqlite3
import pandas as pd
import os
import sqlite3

ex = {
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
 
eval(str(ex))