import unittest
from trivial_purfuit_app.gameboard import GameBoard
from trivial_purfuit_app.token import Token
from trivial_purfuit_app.square.hubsquare import HubSquare

class Token_Test(unittest.TestCase):

    def test_has_category_wedge_none(self):
        # self.player_name = "John"
        # self.color = "blue"
        # self.collected_wedges = []
        # self.location = (4,4)
        # self.last_location = (4,4)
        # self.winning_condition = False
        board = GameBoard()
        token = Token("John","blue")
        collected_wedges = []
        self.assertEqual(collected_wedges, token.has_category_wedge(board.get_current_square(token.player_name).category))

    # def has_all_wedges(self):
    #     #s
    #     pass

    # def set_winning_condition(self):
    #     #
    #     pass

    # def check_winning_condition(self):
    #     #
    #     pass

    # def reset_last_location(self):
    #     #
    #     pass

    # def add_wedge(self, category):
    #     #
    #     pass
    
    # def get_dict(self):
    #     #
    #     pass
        
if __name__ == '__main__':
    unittest.main()