from flask import Flask, request,jsonify
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, мир!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)