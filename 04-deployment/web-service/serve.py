from waitress import serve
from predict import app

if __name__ == '__main__':
    print("Starting the web service...")
    serve(app, host='0.0.0.0', port=9696)