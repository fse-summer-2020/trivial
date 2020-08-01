from trivial_purfuit_app.gamestate import GameState
from uuid import uuid4


class GameInstanceManager:

    instances = {}

    @classmethod
    def get_game_state(cls, session_id):
        if session_id not in cls.instances:
            return None
        else:
            return cls.instances[session_id]

    @classmethod
    def create_game_state(cls):
        session_id = uuid4()
        game_state = GameState()
        cls.instances[session_id] = game_state
        return session_id, game_state
