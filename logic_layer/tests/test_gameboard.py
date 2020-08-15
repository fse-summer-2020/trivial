import unittest
from trivial_purfuit_app.gameboard import GameBoard
from trivial_purfuit_app.token import Token
from trivial_purfuit_app.square.hubsquare import HubSquare
from trivial_purfuit_app.constants import Directions

# data_layer must be running for these tests to run successfully

class GameBoard_Test(unittest.TestCase):

    def test_create_categories(self):
        board = GameBoard()
        self.assertEqual(4, len(board.categories))

    def test_get_current_square(self):
        board = GameBoard()
        token = Token("john", "doe")
        token.location = (4,4)
        square = board.get_current_square(token)
        self.assertTrue(isinstance(square, HubSquare))

    def test_determine_possible_moves_center_last_pos_down(self):
        board = GameBoard()
        token = Token("john", "doe")
        token.location = (4,4)
        token.last_location = (5, 4)
        possible_moves = [Directions.UP, Directions.LEFT, Directions.RIGHT]
        self.assertEqual(possible_moves, board.determine_possible_moves(token))

    def test_determine_possible_moves_center_last_pos_left(self):
        board = GameBoard()
        token = Token("john", "doe")
        token.location = (4,4)
        token.last_location = (4, 3)
        possible_moves = [Directions.DOWN, Directions.UP, Directions.RIGHT]
        self.assertEqual(possible_moves, board.determine_possible_moves(token))

    def test_determine_possible_moves_center_last_pos_right(self):
        board = GameBoard()
        token = Token("john", "doe")
        token.location = (4,4)
        token.last_location = (4, 5)
        possible_moves = [Directions.DOWN, Directions.UP, Directions.LEFT]
        self.assertEqual(possible_moves, board.determine_possible_moves(token))

    def test_determine_possible_moves_center_last_pos_up(self):
        board = GameBoard()
        token = Token("john", "doe")
        token.location = (4,4)
        token.last_location = (3, 4)
        possible_moves = [Directions.DOWN, Directions.LEFT, Directions.RIGHT]
        self.assertEqual(possible_moves, board.determine_possible_moves(token))

    def test_move_token_down(self):
        board = GameBoard()
        token = Token("john", "doe")
        token.location = (4,4)
        board.move_token_location(token, Directions.DOWN)
        self.assertEqual((5,4), token.location)

    def test_move_token_up(self):
        board = GameBoard()
        token = Token("john", "doe")
        token.location = (4,4)
        board.move_token_location(token, Directions.UP)
        self.assertEqual((3,4), token.location)

    def test_move_token_left(self):
        board = GameBoard()
        token = Token("john", "doe")
        token.location = (4,4)
        board.move_token_location(token, Directions.LEFT)
        self.assertEqual((4,3), token.location)

    def test_move_token_right(self):
        board = GameBoard()
        token = Token("john", "doe")
        token.location = (4,4)
        board.move_token_location(token, Directions.RIGHT)
        self.assertEqual((4,5), token.location)

if __name__ == '__main__':
    unittest.main()