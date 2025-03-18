from flask import Flask, request, jsonify
import requests
import os
import random

MODULE_NAME = os.getenv('MODULE_NAME')

app = Flask(__name__)

@app.route("/get_sensors_data", methods=['GET'])
def get_sensors_data():
    radiation = random.randint(0, 4)
    ph = random.randint(0, 14)
    return jsonify({"status": "OK", "radiation":radiation, "ph":ph}), 200

def main():
    print(f'[{MODULE_NAME}] started...')
    app.run(host='0.0.0.0', port=8000, threaded=True)