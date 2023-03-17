#!/usr/bin/env python3
""" API authentication Service"""
from auth import Auth
from flask import (Flask,
                   jsonify,
                   request,
                   abort,
                   redirect)


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world() -> str:
    """ Base route for authentication service API """
    msg = {"message": "Bienvenue"}
    return jsonify(msg)
