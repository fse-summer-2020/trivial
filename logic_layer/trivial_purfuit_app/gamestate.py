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
        # assume answer is a string of the answer
        self.answer_result = self.current_trivia_question.validate_answer(answer)
        idx = self.player_order.index(self.current_player)

        if (self.answer_result == False):
            self.go_to_next_player()
            self.current_state = State.ROLL_DIE
            if (self.current_round == 1):
                for player in self.player_order:
                    if (player.check_winning_condition() == True):
                        if (idx == self.player_order.count - 1):
                            self.current_state = State.GAME_END
                            return self.current_state
            else:
                return self.current_state
        else:
            game_square_type = self.game_board.get_current_square_type()
            if (game_square_type == "CATEGORY"): # ----------------------update definition of category square type
                self.current_state = State.ROLL_DIE
                return self.current_state
            if (game_square_type == "HEADQUARTERS"): # ----------------------update definition of category square type
                 if (self.current_player.has_category_wedge(self.current_trivia_question.category) == False):  #----------how to extract category type from question class?
                     self.current_player.add_wedge(self.current_trivia_question.category) #----------how to extract category type from question class?
                     self.current_state = State.ROLL_DIE
                     return self.current_state
            else:
                if (self.current_player.has_all_wedges() == False):
                     self.current_state = State.ROLL_DIE
                     return self.current_state
                else:
                    self.current_player.set_winning_condition(True)
                    if (self.current_round == 1):
                        if (idx == self.player_order.count - 1):
                            self.current_state = State.GAME_END
                            return self.current_state
                        else:
                            self.go_to_next_player()
                            self.current_state = State.ROLL_DIE
                            return self.current_state
                    else:
                        self.current_state = State.GAME_END
                        return self.current_state

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
    