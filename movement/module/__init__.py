from flask import Flask, request, jsonify
import requests
import os

MODULE_NAME = os.getenv('MODULE_NAME')

app = Flask(__name__)

@app.route('/moveto', methods=['POST'])
def move():
    data = request.get_json()
    x, y = data.get("x"), data.get("y")
    print(f"[{MODULE_NAME}] Moving to coordinates: {x}, {y}")
    return jsonify({"status": "OK", "message": f"Moving to {x}, {y}"}), 200


def main():
    print(f'[{MODULE_NAME}] started...')
    app.run(host='0.0.0.0', port=8000, threaded=True)