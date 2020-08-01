from flask import Blueprint, jsonify, request
from trivial_purfuit_app.game_instance_manager import GameInstanceManager
import json 

logic = Blueprint('logic', __name__, url_prefix='/logic')

@logic.route('/create_game', methods=['POST'])
def create_game():
    players = request.get_json()["players"]
    session_id, game_state = GameInstanceManager.create_game_state()
    state, current_player = game_state.create_game(players)
    print(state)
    return jsonify({"session_id":session_id, "state":state.value, "current_player": current_player.__dict__}), 200