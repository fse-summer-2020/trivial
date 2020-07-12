import requests
from flask import Blueprint, jsonify

url = "http://127.0.0.1:5001/question"
questions = Blueprint('questions', __name__, url_prefix='/question')

@questions.route('/random_question')
def get_random_question():
    return requests.get(url).json(), 200