from .square.headquartersquare import HeadquarterSquare

class GameBoard:
    ROWS = COLS = 9
    board = None

    def __init__(self): #constructor
        self.__create_game_board()

    def __create_game_board(self):
        self.board = [[None for i in range(self.COLS)] for j in range(self.ROWS)] 
        # hq squares at the end of each spoke
        self.board[0][4] = self.board[4][0] = self.board[8][4] = self.board[4][8] = HeadquarterSquare()


    def determine_possible_moves(self, token):
        pass

    # in static, don't think we need it since Token has location
    def get_current_square_for_player(self, token):
        pass

    def get_current_square_type(self):
        self.__create_game_board()