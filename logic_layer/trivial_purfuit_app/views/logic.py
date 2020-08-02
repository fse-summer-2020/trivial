from flask import Blueprint, jsonify, request
from trivial_purfuit_app.game_instance_manager import GameInstanceManager
import json 
from trivial_purfuit_app.constants import State

logic = Blueprint('logic', __name__, url_prefix='/logic')

@logic.route('/create_game', methods=['POST'])
def create_game():
    players = request.get_json()["players"]
    session_id, state = GameInstanceManager.create_game_state(players)
    return jsonify({"session_id":session_id, "state":state}), 200

@logic.route('/answer_trivia', methods=['POST'])
def answer_trivia():
    body = request.get_json()
    session_id = body["session_id"]
    answer = body["answer"]
    game_state = GameInstanceManager.get_game_state(session_id)
    if game_state is None:
        return jsonify({"error":"Game session not found"}), 404
    if game_state.current_state is not State.ANSWER_TRIVIA:
        return jsonify({"error":"Invalid request for current state"}), 409
    state = game_state.answer_trivia(answer)
    return jsonify({"session_id":session_id, "state":state}), 200

@logic.route('/roll_die', methods=['POST'])
def roll_die():
    body = request.get_json()
    session_id = body["session_id"]
    game_state = GameInstanceManager.get_game_state(session_id)
    if game_state is None:
        return jsonify({"error":"Game session not found"}), 404
    if game_state.current_state is not State.ROLL_DIE:
        return jsonify({"error":"Invalid request for current state"}), 409
    state = game_state.get_die_roll()
    return jsonify({"session_id":session_id, "state":state}), 200

@logic.route('/move_direction', methods=['POST'])
def move_direction():
    body = request.get_json()
    session_id = body["session_id"]
    direction = body["direction"]
    game_state = GameInstanceManager.get_game_state(session_id)
    if game_state is None:
        return jsonify({"error":"Game session not found"}), 404
    if game_state.current_state is not State.MOVE_DIRECTION:
        return jsonify({"error":"Invalid request for current state"}), 409
    state = game_state.move_token(direction)
    return jsonify({"session_id":session_id, "state":state}), 200

@logic.route('/set_category', methods=['POST'])
def set_category():
    body = request.get_json()
    session_id = body["session_id"]
    category_id = body["category_id"]
    game_state = GameInstanceManager.get_game_state(session_id)
    if game_state is None:
        return jsonify({"error":"Game session not found"}), 404
    if game_state.current_state not in [State.POLL_CATEGORY_ALL, State.POLL_CATEGORY_CURRENT]:
        return jsonify({"error":"Invalid request for current state"}), 409
    state = game_state.set_category(category_id)
    return jsonify({"session_id":session_id, "state":state}), 200