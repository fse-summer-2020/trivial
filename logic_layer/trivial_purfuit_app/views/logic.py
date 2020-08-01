from flask import Blueprint, jsonify, request
from trivial_purfuit_app.game_instance_manager import GameInstanceManager
import json 
from trivial_purfuit_app.constants import State

logic = Blueprint('logic', __name__, url_prefix='/logic')

@logic.route('/create_game', methods=['POST'])
def create_game():
    players = request.get_json()["players"]
    session_id, game_state = GameInstanceManager.create_game_state()
    state, current_player = game_state.create_game(players)
    print(state)
    return jsonify({"session_id":session_id, "state":state.value, "current_player": current_player.__dict__}), 200

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
    state, current_player = game_state.answer_trivia(answer)
    return jsonify({"session_id":session_id, "state":state.value, "current_player": current_player.__dict__}), 200