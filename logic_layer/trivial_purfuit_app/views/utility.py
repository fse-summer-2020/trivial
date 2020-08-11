import requests
from flask import Blueprint, jsonify, request
from flask_cors import CORS, cross_origin
from trivial_purfuit_app.data_service.data_layer_service import get_all_categories, get_questions_per_cateogry, save_categories, save_questions
utility = Blueprint('utilities', __name__, url_prefix='/utility')

@utility.route('/api_roll_value')
def roll_die():
    url = "http://roll.diceapi.com/json/d4"
    return requests.get(url).json(), 200

@utility.route('/all_categories')
def get_all_categories_view():
    categories = get_all_categories()
    return jsonify(categories), 200


@utility.route('/questions/<category_id>')
def get_questions_per_category_view(category_id):
    questions = get_questions_per_cateogry(category_id)
    return jsonify(questions), 200

@utility.route('/categories', methods=["POST"])
def save_categories_view():
    ids = save_categories(request.get_json())
    return jsonify(ids), 200

@utility.route('/questions', methods=["POST"])
def save_questions_view():
    ids = save_questions(request.get_json())
    return jsonify(ids), 200