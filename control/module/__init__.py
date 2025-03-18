from flask import Flask, request, jsonify
import requests
import os
import random
import time
import threading

MODULE_NAME = os.getenv('MODULE_NAME')
MOVEMENT_URL = "http://movement:8000/moveto"
NAVIGATION_URL = "http://navigation:8000/getcoordinates"

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


@app.route('/log_position', methods=['POST'])
def log_current_pos():
    data = request.get_json()
    x, y = data.get("x"), data.get("y")
    print(f"[{MODULE_NAME}] Received current coordinates from Navigation: x:{x}, y:{y}")
    return jsonify({"status": "OK", "x":x, "y":y}), 200
            
            
def main():
    print(f'[{MODULE_NAME}] started...')
    threading.Thread(target=send_movement_coordinates, daemon=True).start()
    app.run(host='0.0.0.0', port=8000, threaded=True)
    