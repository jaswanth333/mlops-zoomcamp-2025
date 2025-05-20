import os
import pickle
import click
import mlflow

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error


#Setting tracking URI to localhost will set the BACKEND_URI to the local file system
# and the ARTIFACT_URI to the local file system  mentioned in the mlflow ui command
# mlflow ui --backend-store-uri sqlite:///mlruns.db --default-artifact-root ./artifacts
TRACKING_URI = "http://localhost:5000"
EXPERIMENT_NAME='nyc-taxi-experiment'


def load_pickle(filename: str):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)


@click.command()
@click.option(
    "--data_path",
    default="./output",
    help="Location where the processed NYC taxi trip data was saved"
)
def run_train(data_path: str):
    
    with mlflow.start_run():
        mlflow.set_tag("model", "RandomForestRegressor")
        mlflow.sklearn.autolog()
        
        X_train, y_train = load_pickle(os.path.join(data_path, "train.pkl"))
        X_val, y_val = load_pickle(os.path.join(data_path, "val.pkl"))

        rf = RandomForestRegressor(max_depth=10, random_state=0)
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_val)

        rmse = root_mean_squared_error(y_val, y_pred)


if __name__ == '__main__':
    
    mlflow.set_tracking_uri(TRACKING_URI) 
    mlflow.set_experiment(EXPERIMENT_NAME)

    run_train()
