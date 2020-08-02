from .token import Token
from .gameboard import GameBoard
from .constants import State, SquareType
from .models.question_factory_proxy import QuestionFactoryProxy
import requests

class GameState:
    url = "http://roll.diceapi.com/json/d4"

    # self refers to the current object instance. This is implied in java but in python needs to the self reference.

    def __init__(self, players): #constructor
        self.player_order = GameState.get_player_order(players)
        self.game_board = GameBoard() #Easter Egg! - This program is No Trivial Matter!
        self.question_factory_proxy = QuestionFactoryProxy()
        self.current_state = State.ROLL_DIE
        self.current_player = self.player_order[0]
        self.current_round = 1
        self.moves_left = 0
        self.current_trivia_question = None
        self.available_next_squares = None
    
    @classmethod
    def get_player_order(cls, players):
        player_order = []
        for player in players:
            token = Token(player['name'], player['color'])
            player_order.append(token)
        return player_order

    def answer_trivia(self, answer):
        self.answer_result = self.current_trivia_question.validate_answer(answer)
        self.current_trivia_question = None
        idx = self.player_order.index(self.current_player)

        # Start Logic Sequence to Check Answer and Change Game Parameters as Required
        if (self.answer_result == False):
            self.go_to_next_player()
            self.current_state = State.ROLL_DIE
            if (self.current_round == 1):
                for player in self.player_order:
                    if (player.check_winning_condition() == True):
                        if (idx == self.player_order.count - 1):
                            self.current_state = State.GAME_END
                            #return self.current_state, None
                            return self.get_class_dict()
            else:
                #return self.current_state, self.current_player
                return self.get_class_dict()
        else:
            cur_square_type = self.game_board.get_current_square_type(self.current_player)
            if (cur_square_type == SquareType.CATEGORY):
                self.current_state = State.ROLL_DIE
                #return self.current_state, self.current_player
                return self.get_class_dict()

            if (cur_square_type == SquareType.HEADQUARTER):
                 if (self.current_player.has_category_wedge(self.game_board.get_current_square(self.current_player).name) == False):
                     self.current_player.add_wedge(self.game_board.get_current_square(self.current_player).name)
                     self.current_state = State.ROLL_DIE
                     #return self.current_state, self.current_player
                     return self.get_class_dict()
            else:
                if (self.current_player.has_all_wedges() == False):
                     self.current_state = State.ROLL_DIE
                     #return self.current_state, self.current_player
                     return self.get_class_dict()
                else:
                    self.current_player.set_winning_condition(True)
                    if (self.current_round == 1):
                        if (idx == self.player_order.count - 1):
                            self.current_state = State.GAME_END
                            #return self.current_state, None
                            return self.get_class_dict()
                        else:
                            self.go_to_next_player()
                            self.current_state = State.ROLL_DIE
                            #return self.current_state, self.current_player
                            return self.get_class_dict()
                    else:
                        self.current_state = State.GAME_END
                        #return self.current_state, None
                        return self.get_class_dict()

    def get_die_roll(self):
        if (self.current_state == State.ROLL_DIE):
            diedata = requests.get(self.url).json()
            dieside = diedata["dice"]
            self.moves_left = dieside[0].get('value')
            self.available_next_squares = self.game_board.determine_possible_moves(self.current_player)
            self.current_state = State.MOVE_DIRECTION
            #return self.current_player, self.current_state, self.available_next_squares
            return self.get_class_dict()
        else:
             raise Exception("Gamestate has not been set to ROLL_DIE, but get_die_roll has been called")   

    def set_category(self, category):
        if (self.current_state == State.POLL_CATEGORY_ALL or self.current_state == State.POLL_CATEGORY_CURRENT):
            self.current_trivia_question = self.question_factory_proxy.get_question(category)
            self.current_state = State.ANSWER_TRIVIA
            #return self.current_player, self.current_state, self.current_trivia_question
            return self.get_class_dict() 
        else:
            raise Exception("Players should not be choosing which category to pull the question from")


    def go_to_next_player(self):
        idx = self.player_order.index(self.current_player)
        if (idx == len(self.player_order) - 1):
            self.current_player = self.player_order[0]
        else:
            self.current_player = self.player_order[idx+1]

    def move_token(self, direction):
        cur_square_type = self.game_board.get_current_square_type(self.current_player)
        while (self.moves_left > 0):
            if (cur_square_type == SquareType.HEADQUARTER or cur_square_type == SquareType.HUB): #player is on HQ or HUB space
                self.available_next_squares = self.game_board.determine_possible_moves(self.current_player)
                self.current_state = State.MOVE_DIRECTION
                return self.get_class_dict()
            else:
                self.game_board.move_token_location(self.current_player, direction)
                self.moves_left = self.moves_left - 1
    
        if (cur_square_type == SquareType.ROLL_AGAIN_SQUARE): #player is on roll again square
            self.current_state = State.ROLL_DIE
            #return self.current_state, self.current_player
            return self.get_class_dict()
        else:
            if (cur_square_type != SquareType.HEADQUARTER): #player is not on HQ square
                if(self.current_player.has_all_wedges()):
                    self.current_state = State.POLL_CATEGORY_ALL # Poll the players for category choice
                    #return self.current_state, self.current_player
                    return self.get_class_dict()
                else:
                    self.current_state = State.POLL_CATEGORY_CURRENT # Ask current player for category choice
                    #return self.current_state, self.current_player
                    return self.get_class_dict()
            else:
                self.current_trivia_question = self.question_factory_proxy.get_question(self.game_board.get_current_square(self.current_player).name)
                self.current_state = State.ANSWER_TRIVIA
                #return self.current_state, self.current_player
                return self.get_class_dict()

    def get_class_dict(self):
        class_dict = dict()
        class_dict["players"] = [token.get_dict() for token in self.player_order]
        class_dict["current_state"] = self.current_state.value
        class_dict["current_player"] = self.current_player.get_dict()
        class_dict["current_trivia_question"] = self.current_trivia_question.get_dict() if self.current_trivia_question is not None else None
        class_dict["available_next_squares"] = self.available_next_squares
        class_dict["current_round"] = self.current_round
        class_dict["moves_left"] = self.moves_left
        return class_dict   

        # player_order = []
        # current_state = None
        # current_player = None
        # current_trivia_question = None
        # moves_left = None
        # available_next_squares = None
        # current_round = None
        # factory_proxy = None
        # game_board = None
        # url = "http://roll.diceapi.com/json/d4"


