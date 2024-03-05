import sqlalchemy as db
from sqlalchemy import create_engine
import pandas as pd
import sys
import os
import sqlite3
import inspect
from bdd_sqlite.functions import DataBaseV2
from stratégie_nettoyage_donnees import nettoyage_df

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
bdd_path = os.path.join(parentdir, "bdd_sqlite", "db.db")



def charger_donnees(chemin_bdd):

    con = sqlite3.connect(chemin_bdd)
    df = pd.read_sql_query("SELECT * from questionnaires", con)
    con.close()
    print("Le jeu de donnée a été chargé à partir de la base de données.")

    return df



if __name__ == "__main__":
    print(charger_donnees(bdd_path))