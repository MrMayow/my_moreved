from flask import Flask, request, jsonify
import requests
import os
import random
import time
import threading

MODULE_NAME = os.getenv('MODULE_NAME')
CONTROL_LOG_POS_URL = "http://control:8000/log_position"

app = Flask(__name__)


def send_coordinates():
    while True:
        try:
            x, y = random.randint(-100, 100), random.randint(-100, 100)
            print(f"[{MODULE_NAME}] Sent coordinates ({x}, {y}) to Control")
            response = requests.post(CONTROL_LOG_POS_URL, json={"x": x, "y": y})
            print(response)
        except requests.RequestException as e:
            print(f"[{MODULE_NAME}] Error sending coordinates ({x}, {y}): {e}")
        time.sleep(9)

def main():
    print(f'[{MODULE_NAME}] started...')
    threading.Thread(target=send_coordinates, daemon=True).start()
    app.run(host='0.0.0.0', port=8000, threaded=True)