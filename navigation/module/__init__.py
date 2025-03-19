from flask import Flask, request, jsonify
import requests
import os
import random

MODULE_NAME = os.getenv('MODULE_NAME')

app = Flask(__name__)


@app.route('/navigation-data', methods=['GET'])
def get_coordinates():
    x, y = random.randint(-100, 100), random.randint(-100, 100)
    return jsonify({"status": "OK", "x":x, "y":y}), 200


def main():
    print(f'[{MODULE_NAME}] started...')
    app.run(host='0.0.0.0', port=8000, threaded=True)