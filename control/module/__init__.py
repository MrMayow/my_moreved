from flask import Flask, request, jsonify
import requests
import os
import random
import time
import threading

MODULE_NAME = os.getenv('MODULE_NAME')
MOVEMENT_URL = "http://movement:8000/move-to"
NAVIGATION_COORDINATES_URL = "http://navigation:8000/navigation-data"
SENSORS_GET_DATA_URL = "http://sensors:8000/sensors-data"
app = Flask(__name__)

def send_movement_coordinates():
    while True:
        x, y = random.randint(-100, 100), random.randint(-100, 100)
        try:
            print(f"[{MODULE_NAME}] Sent coordinates ({x}, {y}) to Movement.")
            response = requests.post(MOVEMENT_URL, json={"x": x, "y": y})
            response_data = response.json()
            print(f"[{MODULE_NAME}] Response from Movement: {response_data}")
        except requests.RequestException as e:
            print(f"[{MODULE_NAME}] Error sending coordinates ({x}, {y}): {e}")
        time.sleep(7)


def log_sensors_data():
    while True:
        try:
            print(f"[{MODULE_NAME}] Get data from Sensors.")
            response = requests.get(SENSORS_GET_DATA_URL)
            response_data = response.json()

            print(f"[{MODULE_NAME}] Response from Sensors: {response_data}")
        except requests.RequestException as e:
            print(f"[{MODULE_NAME}] Error getting sensors data: {e}")
        time.sleep(12)


@app.route('/navigation-data', methods=['GET'])
def get_current_pos():
    try:
        print(f"[{MODULE_NAME}] Request coordinates from Navigation")
        response = requests.get(NAVIGATION_COORDINATES_URL)
        response_data = response.json()
        x, y = response_data.get("x"), response_data.get("y")
        print(f"[{MODULE_NAME}] Received current coordinates from Navigation: x:{x}, y:{y}")
        return jsonify({"status": "OK", "x":x, "y":y})
    except requests.RequestException as e:
        print(f"[{MODULE_NAME}] Error getting coordinates: {e}")
    return jsonify({"status": "NO RESULT"})
    
 
@app.route('/ecological-data', methods=['GET'])
def get_ecological_data():
    try:
        print(f"[{MODULE_NAME}] Request ecological data from Sensors")
        response = requests.get(SENSORS_GET_DATA_URL)
        response_data = response.json()
        radiation, ph = response_data.get("radiation"), response_data.get("ph")
        print(f"[{MODULE_NAME}] Received ecological data from Sensors: radiation:{radiation}, ph:{ph}")
        return jsonify({"status": "OK", "radiation":radiation, "ph":ph})
    except requests.RequestException as e:
        print(f"[{MODULE_NAME}] Error getting ecological data: {e}")
    return jsonify({"status": "NO RESULT"})

            
def main():
    print(f'[{MODULE_NAME}] started...')
    #threading.Thread(target=send_movement_coordinates, daemon=True).start()
    #threading.Thread(target=log_sensors_data, daemon=True).start()
    app.run(host='0.0.0.0', port=8000, threaded=True)
    