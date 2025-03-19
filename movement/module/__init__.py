from flask import Flask, request, jsonify
import requests
import os

MODULE_NAME = os.getenv('MODULE_NAME')

app = Flask(__name__)

@app.route('/move-to', methods=['POST'])
def move():
    data = request.get_json()
    route = list(data.get("route"))
    print(f"[{MODULE_NAME}] Setup route: {route}")
    return jsonify({"status": "OK"}), 200


def main():
    print(f'[{MODULE_NAME}] started...')
    app.run(host='0.0.0.0', port=8000, threaded=True)