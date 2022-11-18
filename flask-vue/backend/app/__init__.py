import flask.json, json, os, inspect
from flask import Flask, jsonify, request, Response

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# API GET routes

if __name__ == "__main__":
    app.run(host='0.0.0.0')
