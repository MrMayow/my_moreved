from flask import Flask, request, jsonify
import requests
import os
import threading
import time

MODULE_NAME = os.getenv('MODULE_NAME')
CONTROL_COORDINATES_URL = "http://control:8000/get_coordinates"
app = Flask(__name__)

def send_coordinates_to_ORDV():
    while True:
        try:
            print(f"[{MODULE_NAME}] ORDV request coordinates")
            response = requests.get(CONTROL_COORDINATES_URL)
            response_data = response.json()
            x, y = response_data.get("x"), response_data.get("y")
            print(f"[{MODULE_NAME}] Send coordinates to ORDV x:{x}, y:{y}")
            
        except requests.RequestException as e:
            print(f"[{MODULE_NAME}] Error getting coordinates: {e}")
        time.sleep(5)

def main():
    print(f'[{MODULE_NAME}] started...')
    threading.Thread(target=send_coordinates_to_ORDV, daemon=True).start()
    app.run(host='0.0.0.0', port=8000, threaded=True)