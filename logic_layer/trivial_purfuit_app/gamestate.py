from .token import Token
from .gameboard import GameBoard
from .constants import State, SquareType
from .models.question_factory_proxy import QuestionFactoryProxy
import requests

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
    url = "http://roll.diceapi.com/json/d4"

    # self refers to the current object instance. This is implied in java but in python needs to the self reference.

    def __init__(self): #constructor
        pass
    
    def create_game(self, players):
        self.set_player_order(players)
        self.game_board = GameBoard() #Easter Egg!
        self.question_factory_proxy = QuestionFactoryProxy()
        self.current_state = State.ROLL_DIE
        self.current_player = self.player_order[0]
        self.current_round = 1
        #return self.current_state, self.current_player
        return self.get_class_dict()

    def set_player_order(self, players):
        for player in players:
            token = Token(player['name'], player['color'])
            self.player_order.append(token) #assume list order is the order of play already

    def answer_trivia(self, answer):
        # assume answer is a string of the answer
        self.answer_result = self.current_trivia_question.validate_answer(answer)
        self.current_trivia_question = None
        idx = self.player_order.index(self.current_player)

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
            if (cur_square_type == SquareType.CATEGORY): # ----------------------update definition of category square type
                self.current_state = State.ROLL_DIE
                #return self.current_state, self.current_player
                return self.get_class_dict()
                
            if (cur_square_type == SquareType.HEADQUARTER): # ----------------------update definition of category square type
                 if (self.current_player.has_category_wedge(self.current_trivia_question.category) == False):  #get categetoy from SPACE LOCATION nottttt question
                     self.current_player.add_wedge(self.current_trivia_question.category)   #get categetoy from SPACE LOCATION nottttt question
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
        diedata = requests.get(self.url).json()
        dieside = diedata["dice"]
        dieValue = dieside[0].get('value')
        return dieValue

    def set_category(self, category):
        ################################################################
        self.current_trivia_question = self.question_factory_proxy.get_question(category)
        #check sequence diagram fro missing fucntions and addd them!
        #Add to the blueprints if this is not the returned value:
        #return self.current_state, self.current_player
        #when we set state to poll, the prez layer sets question based on categroy (set question from category)
        ################################################################
        pass 

    def go_to_next_player(self):
        idx = self.player_order.index(self.current_player)
        if (idx == len(self.player_order) - 1):
            self.current_player = self.player_order[0]
        else:
            self.current_player = self.player_order[idx+1]

    def move_token(self, direction):
        ################################################################
        #Add to the blueprints if this is not the returned value:
        #return self.current_state, self.current_player
        ################################################################

        cur_square_type = self.game_board.get_current_square_type(self.current_player)
        while (self.moves_left >= 0):
            if (cur_square_type == SquareType.HEADQUARTER): #PLAYER IS AT INTERSECTION
                #determine possible moves to gameboard (return square)
                self.current_state = State.MOVE_DIRECTION
                #return self.current_state, self.current_player
                return self.get_class_dict()
            else:
                #TODO - actually move the player
                return self.current_state, self.current_player
                #move player direction to gameboard (return square)

        if (cur_square_type == SquareType.ROLL_AGAIN_SQUARE): #player is on roll again square
            self.current_state = State.ROLL_DIE
            #return self.current_state, self.current_player
            return self.get_class_dict()
        else:
            if (cur_square_type != SquareType.HEADQUARTER): #player is not on HQ square
                if(self.current_player.has_all_wedges()): #check if they have all wedges -> to token class
                    self.current_state = State.POLL_CATEGORY_ALL #if they have them all == TRUE poll the players
                    #return self.current_state, self.current_player
                    return self.get_class_dict()
                else:
                    self.current_state = State.POLL_CATEGORY_CURRENT #let them get a random category?
                    #return self.current_state, self.current_player
                    return self.get_class_dict()
            else:
                #get categroy suqure from gaembaord
                #get question category from game factory proxy
                    #this have to calll a random quesiton (make function in question factory to get random question VR specific catgetory)
                self.question_factory_proxy.get_question(self.game_board.get_current_square(self.current_player).name)
                self.current_state = State.ANSWER_TRIVIA
                #return self.current_state, self.current_player
                return self.get_class_dict()

    def get_class_dict(self):
        class_dict = self.__dict__
        items_to_remove = ['player_order', 'factory_proxy', 'game_board', 'url']
        [class_dict.pop(key) for key in items_to_remove] 
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


