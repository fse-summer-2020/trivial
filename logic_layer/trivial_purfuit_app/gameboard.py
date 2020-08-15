from .square.headquartersquare import HeadquarterSquare
from .square.roll_again_square import RollAgainSquare
from .square.hubsquare import HubSquare
from .square.categorysquare import CategorySquare
from .constants import Directions

from trivial_purfuit_app.data_service.data_layer_service import get_all_categories
from .models.category import Category

class GameBoard:
    ROWS = COLS = 9

    def __init__(self): #constructor
        self.categories = []
        self.board = None
        self.get_and_create_categories()
        self.__create_game_board()
    
    # WHITE = 0
    # RED = 1
    # GREEN = 2 
    # BLUE = 3

    #    0   1   2   3   4   5   6   7   8   
    #0   W   R   RA  B   HQ  B   RA  R   G
    #1   B               B               W   
    #2   RA              R               RA
    #3   G               W               R
    #4   HQ  G   B   R   H   G   W   R   HQ           
    #5   G               B               R
    #6   RA              G               RA
    #7   B               W               W
    #8   R   G   RA  W   HQ  W   RA  G   B

    def __create_game_board(self):
        self.board = [[None for i in range(self.COLS)] for j in range(self.ROWS)] 

        # hq squares at the end of each spoke
        # TODO: adjust categories as needed to comply with game board rules
        self.board[0][4] = HeadquarterSquare(self.categories[0])
        self.board[4][0] = HeadquarterSquare(self.categories[1])
        self.board[8][4] = HeadquarterSquare(self.categories[3])
        self.board[4][8] = HeadquarterSquare(self.categories[2])

        # roll again squares
        self.board[0][2] = RollAgainSquare()
        self.board[0][6] = RollAgainSquare()
        self.board[2][0] = RollAgainSquare()
        self.board[2][8] = RollAgainSquare()
        self.board[6][8] = RollAgainSquare()
        self.board[6][0] = RollAgainSquare()
        self.board[8][2] = RollAgainSquare()
        self.board[8][6] = RollAgainSquare()

        # hub square
        self.board[4][4] = HubSquare()

        # category squares
        # TODO: adjust categories as needed to comply with game board rules
        self.board[0][0] = CategorySquare(self.categories[0])
        self.board[0][1] = CategorySquare(self.categories[1])
        self.board[0][3] = CategorySquare(self.categories[3])
        self.board[0][5] = CategorySquare(self.categories[3])
        self.board[0][7] = CategorySquare(self.categories[1])
        self.board[0][8] = CategorySquare(self.categories[2])

        self.board[1][0] = CategorySquare(self.categories[3])
        self.board[1][4] = CategorySquare(self.categories[3])
        self.board[1][8] = CategorySquare(self.categories[0])

        self.board[2][4] = CategorySquare(self.categories[1])

        self.board[3][0] = CategorySquare(self.categories[2])
        self.board[3][4] = CategorySquare(self.categories[0])
        self.board[3][8] = CategorySquare(self.categories[1])

        self.board[4][1] = CategorySquare(self.categories[2])
        self.board[4][2] = CategorySquare(self.categories[3])
        self.board[4][3] = CategorySquare(self.categories[1])
        self.board[4][5] = CategorySquare(self.categories[2])
        self.board[4][6] = CategorySquare(self.categories[0])
        self.board[4][7] = CategorySquare(self.categories[1])

        self.board[5][0] = CategorySquare(self.categories[2])
        self.board[5][4] = CategorySquare(self.categories[3])
        self.board[5][8] = CategorySquare(self.categories[1])

        self.board[6][4] = CategorySquare(self.categories[2])

        self.board[7][0] = CategorySquare(self.categories[3])
        self.board[7][4] = CategorySquare(self.categories[0])
        self.board[7][8] = CategorySquare(self.categories[0])

        self.board[8][0] = CategorySquare(self.categories[1])
        self.board[8][1] = CategorySquare(self.categories[2])
        self.board[8][3] = CategorySquare(self.categories[0])
        self.board[8][5] = CategorySquare(self.categories[0])
        self.board[8][7] = CategorySquare(self.categories[2])
        self.board[8][8] = CategorySquare(self.categories[3])

    def determine_possible_moves(self, token):
        xPos = token.location[0]
        yPos = token.location[1]
        
        last_xPos = token.last_location[0]
        last_yPos = token.last_location[1]

        possible_moves = []
        #check down
        if xPos < 8 and (self.board[xPos+1][yPos] is not None) and (xPos+1 != last_xPos):
            possible_moves.append(Directions.DOWN)

        #check up
        if xPos > 0 and (self.board[xPos-1][yPos] is not None) and (xPos-1 != last_xPos):
            possible_moves.append(Directions.UP)

        #check left
        if yPos > 0 and (self.board[xPos][yPos-1] is not None) and (yPos-1 != last_yPos):
            possible_moves.append(Directions.LEFT)

        #check right
        if yPos < 8 and (self.board[xPos][yPos+1] is not None) and (yPos+1 != last_yPos):
            possible_moves.append(Directions.RIGHT)

        return possible_moves

    def get_current_square(self, token):
        xPos = token.location[0]
        yPos = token.location[1]
        return self.board[xPos][yPos]

    def get_and_create_categories(self):
        category_json = get_all_categories()
        for item in category_json:
            self.categories.append(Category(item["name"], item["_id"], item["color"]))
        

    def move_token_location(self, token, direction):
        #update direction if token is in a corner
        if (token.location == (0,0)):
            if (token.last_location == (0,1)): #current direction would be LEFT approaching corner
                direction = Directions.DOWN
            else:
                direction = Directions.RIGHT
        elif (token.location == (0,8)):
            if (token.last_location == (0,7)): #current direction would be RIGHT approaching corner
                direction = Directions.DOWN
            else:
                direction = Directions.LEFT
        elif (token.location == (8,0)):
            if (token.last_location == (7,0)): #current direction would be DOWN approaching corner
                direction = Directions.RIGHT
            else:
                direction = Directions.UP
        elif (token.location == (8,8)):
            if (token.last_location == (8,7)): #current direction would be RIGHT approaching corner
                direction = Directions.UP
            else:
                direction = Directions.LEFT

        #set old location to current location before updating to new location
        token.last_location = (token.location[0], token.location[1])

        # actually move the token now
        if (direction == Directions.LEFT):
            token.location = (token.location[0], token.location[1]-1)
        elif (direction == Directions.RIGHT):
            token.location = (token.location[0], token.location[1]+1)
        elif (direction == Directions.UP):
            token.location = (token.location[0]-1, token.location[1])
        elif (direction == Directions.DOWN):
            token.location = (token.location[0]+1, token.location[1])
        else :
            raise Exception("Direction Choosen is Not Valid")
        return direction