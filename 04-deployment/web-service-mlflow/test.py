import requests

if __name__ == "__main__":
    ride = {
        "PULocationID": 10,
        "DOLocationID": 50,
        "trip_distance": 40
    }

    url = 'http://localhost:9696/predict'

    try:
        response = requests.post(url, json=ride)
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
    finally:
        print(response.json())
