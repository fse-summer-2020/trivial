from .square.headquartersquare import HeadquarterSquare
from .square.roll_again_square import RollAgainSquare
from .square.hubsquare import HubSquare
from .square.categorysquare import CategorySquare

from trivial_purfuit_app.data_service.data_layer_service import get_all_categories
from .models.category import Category

class GameBoard:
    ROWS = COLS = 9
    board = None
    categories = []

    def __init__(self): #constructor
        self.get_and_create_categories()
        self.__create_game_board()
    
    #    0   1   2   3   4   5   6   7   8   
    #0   C   C   RA  C   HQ  C   RA  C   C
    #1   RA              C               C   
    #2   C               C               RA
    #3   C               C               C
    #4   HQ  C   C   C   H   C   C   C   HQ           
    #5   C               C               RA
    #6   C               C               C
    #7   RA              C               C
    #8   C   C   RA  C   HQ  C   RA  C   C
    def __create_game_board(self):
        self.board = [[None for i in range(self.COLS)] for j in range(self.ROWS)] 

        # hq squares at the end of each spoke
        self.board[0][4] = HeadquarterSquare()
        self.board[4][0] = HeadquarterSquare()
        self.board[8][4] = HeadquarterSquare()
        self.board[4][8] = HeadquarterSquare()

        # roll again squares
        self.board[0][2] = RollAgainSquare()
        self.board[0][6] = RollAgainSquare()
        self.board[1][0] = RollAgainSquare()
        self.board[2][8] = RollAgainSquare()
        self.board[5][8] = RollAgainSquare()
        self.board[7][0] = RollAgainSquare()
        self.board[8][2] = RollAgainSquare()
        self.board[8][6] = RollAgainSquare()

        # hub square
        self.board[4][4] = HubSquare()

        # category squares
        # TODO: adjust categories as needed to comply with game board rules
        self.board[0][0] = CategorySquare(self.categories[0])
        self.board[0][1] = CategorySquare(self.categories[0])
        self.board[0][3] = CategorySquare(self.categories[0])
        self.board[0][5] = CategorySquare(self.categories[0])
        self.board[0][7] = CategorySquare(self.categories[0])
        self.board[0][8] = CategorySquare(self.categories[0])

        self.board[1][8] = CategorySquare(self.categories[0])

        self.board[2][0] = CategorySquare(self.categories[0])

        self.board[3][0] = CategorySquare(self.categories[0])
        self.board[3][8] = CategorySquare(self.categories[0])

        self.board[4][1] = CategorySquare(self.categories[0])
        self.board[4][2] = CategorySquare(self.categories[0])
        self.board[4][3] = CategorySquare(self.categories[0])
        self.board[4][5] = CategorySquare(self.categories[0])
        self.board[4][6] = CategorySquare(self.categories[0])
        self.board[4][7] = CategorySquare(self.categories[0])

        self.board[5][0] = CategorySquare(self.categories[0])

        self.board[6][0] = CategorySquare(self.categories[0])
        self.board[6][8] = CategorySquare(self.categories[0])

        self.board[7][8] = CategorySquare(self.categories[0])

        self.board[8][0] = CategorySquare(self.categories[0])
        self.board[8][1] = CategorySquare(self.categories[0])
        self.board[8][3] = CategorySquare(self.categories[0])
        self.board[8][5] = CategorySquare(self.categories[0])
        self.board[8][7] = CategorySquare(self.categories[0])
        self.board[8][8] = CategorySquare(self.categories[0])

    def determine_possible_moves(self, token):
        xPos = token.location[0]
        yPos = token.location[1]
        
        last_xPos = token.last_location[0]
        last_yPos = token.last_location[1]

        possible_moves = []

        #check down
        if (self.board[xPos+1] is not None) and (xPos+1 != last_xPos):
            possible_moves.append((xPos+1, yPos))

        #check up
        if (self.board[xPos-1] is not None) and (xPos-1 != last_xPos):
            possible_moves.append((xPos-1, yPos))

        #check left
        if (self.board[yPos-1] is not None) and (yPos-1 != last_yPos):
            possible_moves.append((xPos, yPos-1))

        #check right
        if (self.board[yPos+1] is not None) and (yPos+1 != last_yPos):
            possible_moves.append((xPos, yPos+1))

        return possible_moves
            

    def get_current_square_type(self, token):
        xPos = token.location[0]
        yPos = token.location[1]
        return type(self.board[xPos][yPos]).__name__

    def get_and_create_categories(self):
        category_json = get_all_categories()
        for item in category_json:
            self.categories.append(Category(item["name"]))