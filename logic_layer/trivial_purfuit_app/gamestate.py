from token import Token
from gameboard import GameBoard
from state import State

class GameState:
    player_order = []
    current_state = None
    current_player = None
    current_trivia_question = None
    moves_left = None
    available_next_squares = None
    current_round = None
    factory_proxy = None
    game_board = None

    # self refers to the current object instance. This is implied in java but in python needs to the self reference.

    def __init__(self): #constructor
        pass
    
    def create_game(self, players):
        self.set_player_order(players)
        self.game_board = GameBoard() #Easter Egg!
        #new_factory_proxy #new factory proxy class
        self.current_state = State.ROLL_DIE
        self.current_player = self.player_order[0]
        self.current_round = 1
        return self.current_state

    def set_player_order(self, players):
        for player in players:
            token = Token(player.name, player.color)
            self.player_order.append(token) #assume list order is the order of play already

    def answer_trivia(self, answer):
        pass

    def get_die_roll(self):
        # call the DieRollAPI
        pass

    def set_category(self, category):
        pass 

    def go_to_next_player(self):
        idx = self.player_order.index(self.current_player)
        if (idx == self.player_order.count - 1):
            self.current_player = self.player_order[0]
        else:
            self.current_player = self.player_order[idx+1]

    def move_token(self, direction): #this should reference token we're trying to move...right? the sequence diagram has a direction listed too?
        pass
    