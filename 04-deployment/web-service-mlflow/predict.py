import mlflow
from flask import Flask, request, jsonify

from mlflow.tracking import MlflowClient


MLFLOW_TRACKING_URI = 'http://localhost:5000'

client = MlflowClient(tracking_uri=MLFLOW_TRACKING_URI)

experiment = client.get_experiment_by_name("green-taxi-duration")
runs = client.search_runs(experiment_ids=[experiment.experiment_id], order_by=["start_time DESC"], max_results=1)
RUN_ID = runs[0].info.run_id

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

model_uri = f'runs:/{RUN_ID}/model'
model = mlflow.pyfunc.load_model(model_uri)


def prepare_features(ride):
    features = {}
    features['PU_DO'] = '%s_%s' % (ride['PULocationID'], ride['DOLocationID'])
    features['trip_distance'] = ride['trip_distance']
    return features


def predict(features):
    preds = model.predict(features)
    return float(preds[0])


app = Flask('duration-prediction')


@app.route('/predict', methods=['POST'])
def predict_endpoint():
    ride = request.get_json()

    features = prepare_features(ride)
    pred = predict(features)

    result = {
        'duration': pred,
        'model_version': RUN_ID
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
