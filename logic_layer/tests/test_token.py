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
        current_square_category = self.board.get_current_square(self.token).category
        has_category_wedge = self.token.has_category_wedge(current_square_category)
        self.assertFalse(has_category_wedge)

    def test_has_category_wedge_one(self):
        cat = Category("places","1", "blue")
        self.token.add_wedge(cat)
        self.assertTrue(self.token.has_category_wedge(cat))

    def test_has_all_wedges_true(self):
        cat1 = Category("places","1", "blue")
        cat2 = Category("people","2", "green")
        cat3 = Category("events","3", "red")
        cat4 = Category("holidays","4", "white")
        self.token.add_wedge(cat1);
        self.token.add_wedge(cat2);
        self.token.add_wedge(cat3);
        self.token.add_wedge(cat4);
        self.assertTrue(self.token.has_all_wedges())

    def test_has_all_wedges_false(self):
        self.assertFalse(self.token.has_all_wedges())

if __name__ == '__main__':
    unittest.main()