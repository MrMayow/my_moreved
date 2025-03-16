from flask import Flask, request, jsonify
import requests
import os
import random
import time
import threading

MODULE_NAME = os.getenv('MODULE_NAME')
MOVEMENT_URL = "http://movement:8000/moveto"
NAVIGATION_URL = "http://navigation:8000/getcoordinates"
COORDINATES = [(10, 20), (15, 25), (30, 40)]  

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

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

def log_current_pos():
    while True:
        try:
            print(f"[{MODULE_NAME}] Sent coordinates request to Navigation")
            response = requests.get(NAVIGATION_URL)
            response_data = response.json()
            x, y = response_data.get("x"), response_data.get("y")
            print(f"[{MODULE_NAME}] Response from Navigation: {response_data}")
        except requests.exceptions.RequestException as e:
            print(f"[{MODULE_NAME}] Failed to get data: {e}")
        time.sleep(10)
    


def main():
    print(f'[{MODULE_NAME}] started...')
    threading.Thread(target=send_movement_coordinates, daemon=True).start()
    threading.Thread(target=log_current_pos, daemon=True).start()
    app.run(host='0.0.0.0', port=8000, threaded=True)
    