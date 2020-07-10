from flask import Blueprint, jsonify

questions = Blueprint('questions', __name__, url_prefix='/question')

@questions.route('/random_question')
def get_random_question():
    return jsonify({"question":"???"}), 200