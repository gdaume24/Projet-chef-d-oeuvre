import sqlalchemy as db
from functions import DataBaseV2
from sqlalchemy import create_engine
import pandas as pd
import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from stratégie_nettoyage_donnees import nettoyage_df
data_path = os.path.join(parentdir, "data/survey.csv")

engine = create_engine(f'sqlite:///{currentdir}/db.db', echo=False)
df = pd.read_csv(data_path)
df = nettoyage_df(df)
df.to_sql('questionnaires', con=engine, if_exists='fail', index=False)
print("Les données ont été ajoutées en base.")
