import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'scikit-learn==1.6.1'])



import pickle
import pandas as pd
import os

current_path = os.path.dirname(os.path.abspath(__file__))
print(f"Current file path: {current_path}")

with open('/workspaces/mlops-zoomcamp-2025/cohorts/2025/04-deployment/homework/model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)

categorical = ['PULocationID', 'DOLocationID']

def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df


df = read_data('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-03.parquet')


dicts = df[categorical].to_dict(orient='records')
X_val = dv.transform(dicts)
y_pred = model.predict(X_val)
