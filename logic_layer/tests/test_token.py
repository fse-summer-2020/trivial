import unittest
from trivial_purfuit_app.gameboard import GameBoard
from trivial_purfuit_app.token import Token
from trivial_purfuit_app.square.hubsquare import HubSquare
from trivial_purfuit_app.models.category import Category

class Token_Test(unittest.TestCase):


    def setUp(self):
        self.collected_wedges = []
        self.board = GameBoard()
        self.token = Token("john", "doe")
        self.token.location = (3,4)

    def test_has_category_wedge_none(self):
        self.assertFalse(self.token.has_category_wedge(self.board.get_current_square(self.token).category))
        # self.assertEqual(collected_wedges, self.token.has_category_wedge(self.board.get_current_square(self.token).category))

    def test_has_category_wedge_one(self):
        cat = Category("Places","Dksnn34", "Blue")
        self.token.add_wedge(cat)
        self.assertTrue(self.token.has_category_wedge(cat))

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