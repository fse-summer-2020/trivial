import unittest
from trivial_purfuit_app.gameboard import GameBoard
from trivial_purfuit_app.token import Token
from trivial_purfuit_app.square.hubsquare import HubSquare
from trivial_purfuit_app.constants import Directions

# data_layer must be running for these tests to run successfully

class GameBoard_Test(unittest.TestCase):

    def setUp(self):
        self.board = GameBoard()
        self.token = Token("john", "doe")
        self.token.location = (4,4)

    def test_create_categories(self):
        self.assertEqual(4, len(self.board.categories))

    def test_get_current_square(self):
        square = self.board.get_current_square(self.token)
        self.assertTrue(isinstance(square, HubSquare))

    def test_determine_possible_moves_center_last_pos_down(self):
        self.token.last_location = (5, 4)
        possible_moves = [Directions.UP, Directions.LEFT, Directions.RIGHT]
        self.assertEqual(possible_moves, self.board.determine_possible_moves(self.token))

    def test_determine_possible_moves_center_last_pos_left(self):
        self.token.last_location = (4, 3)
        possible_moves = [Directions.DOWN, Directions.UP, Directions.RIGHT]
        self.assertEqual(possible_moves, self.board.determine_possible_moves(self.token))

    def test_determine_possible_moves_center_last_pos_right(self):
        self.token.last_location = (4, 5)
        possible_moves = [Directions.DOWN, Directions.UP, Directions.LEFT]
        self.assertEqual(possible_moves, self.board.determine_possible_moves(self.token))

    def test_determine_possible_moves_center_last_pos_up(self):
        self.token.last_location = (3, 4)
        possible_moves = [Directions.DOWN, Directions.LEFT, Directions.RIGHT]
        self.assertEqual(possible_moves, self.board.determine_possible_moves(self.token))

    def test_move_token_down(self):
        self.board.move_token_location(self.token, Directions.DOWN)
        self.assertEqual((5,4), self.token.location)

    def test_move_token_up(self):
        self.board.move_token_location(self.token, Directions.UP)
        self.assertEqual((3,4), self.token.location)

    def test_move_token_left(self):
        self.board.move_token_location(self.token, Directions.LEFT)
        self.assertEqual((4,3), self.token.location)

    def test_move_token_right(self):
        self.board.move_token_location(self.token, Directions.RIGHT)
        self.assertEqual((4,5), self.token.location)

if __name__ == '__main__':
    unittest.main()