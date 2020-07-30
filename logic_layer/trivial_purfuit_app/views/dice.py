import requests
from flask import Blueprint, jsonify

url = "http://roll.diceapi.com/json/d4"
roll = Blueprint('roll', __name__, url_prefix='/roll')

@roll.route('/')
def roll_die():
    return requests.get(url).json(), 200