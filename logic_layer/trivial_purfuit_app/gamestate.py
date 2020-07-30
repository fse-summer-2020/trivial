class GameState:
    player_order = None
    current_state = None
    current_player = None
    current_trivia_question = None
    moves_left = None
    available_next_squares = None
    current_round = None
    factory_proxy = None

    # self refers to the current object instance. This is implied in java but in python needs to the self reference.

    def __init__(self): #constructor
        pass
    
    def answer_trivia(self, answer):
        pass

    def getDieRoll(self):
        pass

    def set_category(self, category):
        pass 

    def go_to_next_player(self):
        pass

    def move_token(self, token):
        pass
    