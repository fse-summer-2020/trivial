import requests
from flask import Blueprint, jsonify
from flask_cors import CORS, cross_origin

utility = Blueprint('utilities', __name__, url_prefix='/utility')

@utility.route('/api_roll_value')
def roll_die():
    url = "http://roll.diceapi.com/json/d4"
    return requests.get(url).json(), 200

@utility.route('/all_categories')
def get_all_categories():
    url = "http://127.0.0.1:5001/category"
    return requests.get(url).json(), 200

@utility.route('/questions/<category_id>')
def get_questions_per_category(category_id):
    print(category_id)
    url = "http://127.0.0.1:5001/question?category_id=" + category_id
    return requests.get(url).json(), 200