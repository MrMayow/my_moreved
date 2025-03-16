from flask import Flask, request, jsonify
import requests
import os
import random
import time

MODULE_NAME = os.getenv('MODULE_NAME')
CONTROL_URL = "http://control:8000/currentpos"

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

@app.route('/getcoordinates', methods=['GET'])
def get__coordinates():
    x, y = random.randint(-100, 100), random.randint(-100, 100)
    print(f"[{MODULE_NAME}] Sent coordinates ({x}, {y}) to Control")
    return jsonify({"status": "OK", "x":x, "y":y}), 200


def main():
    print(f'[{MODULE_NAME}] started...')
    app.run(host='0.0.0.0', port=8000, threaded=True)