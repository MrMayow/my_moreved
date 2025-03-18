from flask import Flask, request, jsonify
import requests
import os

MODULE_NAME = os.getenv('MODULE_NAME')

app = Flask(__name__)

def main():
    print(f'[{MODULE_NAME}] started...')
    app.run(host='0.0.0.0', port=8000, threaded=True)