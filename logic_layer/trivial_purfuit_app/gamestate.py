from .token import Token
from .gameboard import GameBoard
from .constants import State, SquareType

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
        return self.current_state, self.current_player

    def set_player_order(self, players):
        for player in players:
            token = Token(player['name'], player['color'])
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
                            return self.current_state, None
            else:
                return self.current_state, self.current_player
        else:
            cur_square_type = self.game_board.get_current_square_type(self.current_player)
            if (cur_square_type == SquareType.CATEGORY): # ----------------------update definition of category square type
                self.current_state = State.ROLL_DIE
                return self.current_state, self.current_player
            if (cur_square_type == SquareType.HEADQUARTER): # ----------------------update definition of category square type
                 if (self.current_player.has_category_wedge(self.current_trivia_question.category) == False):  #----------how to extract category type from question class?
                     self.current_player.add_wedge(self.current_trivia_question.category) #----------how to extract category type from question class?
                     self.current_state = State.ROLL_DIE
                     return self.current_state, self.current_player
            else:
                if (self.current_player.has_all_wedges() == False):
                     self.current_state = State.ROLL_DIE
                     return self.current_state, self.current_player
                else:
                    self.current_player.set_winning_condition(True)
                    if (self.current_round == 1):
                        if (idx == self.player_order.count - 1):
                            self.current_state = State.GAME_END
                            return self.current_state, None
                        else:
                            self.go_to_next_player()
                            self.current_state = State.ROLL_DIE
                            return self.current_state, self.current_player
                    else:
                        self.current_state = State.GAME_END
                        return self.current_state, None

    def get_die_roll(self):
        # call the DieRollAPI
        pass

    def set_category(self, category):
        pass 

    def go_to_next_player(self):
        idx = self.player_order.index(self.current_player)
        if (idx == len(self.player_order) - 1):
            self.current_player = self.player_order[0]
        else:
            self.current_player = self.player_order[idx+1]

    def move_token(self, direction):
        cur_square_type = self.game_board.get_current_square_type(self.current_player)
        while (self.moves_left >= 0):
            if (cur_square_type == SquareType.HEADQUARTER): #PLAYER IS AT INTERSECTION
                #determine possible moves to gameboard (return square)
                self.current_state = State.MOVE_DIRECTION
                return self.current_state
            else:
                return None
                #move player direction to gameboard (return square)

        if (cur_square_type == SquareType.ROLL_AGAIN_SQUARE): #player is on roll again square
            self.current_state = State.ROLL_DIE
            return self.current_state
        else:
            if (cur_square_type != SquareType.HEADQUARTER): #player is not on HQ square
                if(self.current_player.has_all_wedges()): #check if they have all wedges -> to token class
                    self.current_state = State.POLL_CATEGORY_ALL #if they have them all == TRUE poll the players
                    return self.current_state
                else:
                    self.current_state = State.POLL_CATEGORY_CURRENT #let them get a random category?
                    return self.current_state
            else:
                #get categroy suqure from gaembaord
                #get question category from game factory proxy
                    #this have to calll a random quesiton (make function in question factory to get random question VR specific catgetory)
                self.current_state = State.ANSWER_TRIVIA
                return self.current_state


