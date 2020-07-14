import requests
from flask import Blueprint, jsonify
from flask_cors import CORS, cross_origin

url = "http://127.0.0.1:5001/question"
questions = Blueprint('questions', __name__, url_prefix='/question')
CORS(questions)

@questions.route('/random_question')
def get_random_question():
    return requests.get(url).json(), 200