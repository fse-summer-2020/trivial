import unittest
from trivial_purfuit_app.gameboard import GameBoard
from trivial_purfuit_app.token import Token
from trivial_purfuit_app.square.hubsquare import HubSquare

class GameBoard_Test(unittest.TestCase):

    def test_create_categories(self):
        board = GameBoard()
        self.assertEqual(4, len(board.categories))

    def test_get_current_square_type(self):
        board = GameBoard()
        token = Token("john", "doe")
        token.location = (4,4)
        self.assertEqual(type(HubSquare()).__name__, board.get_current_square_type(token))

    def test_determine_possible_moves_center_last_pos_down(self):
        board = GameBoard()
        token = Token("john", "doe")
        token.location = (4,4)
        token.last_location = (5, 4)
        possible_moves = [(3, 4), (4, 3), (4, 5)]
        self.assertEqual(possible_moves, board.determine_possible_moves(token))

    def test_determine_possible_moves_center_last_pos_left(self):
        board = GameBoard()
        token = Token("john", "doe")
        token.location = (4,4)
        token.last_location = (4, 3)
        possible_moves = [(3, 4), (5, 4), (4, 5)]
        self.assertEqual(possible_moves, board.determine_possible_moves(token))

    def test_determine_possible_moves_center_last_pos_right(self):
        board = GameBoard()
        token = Token("john", "doe")
        token.location = (4,4)
        token.last_location = (4, 5)
        possible_moves = [(5, 4), (3, 4), (4, 3)]
        self.assertEqual(possible_moves, board.determine_possible_moves(token))

    def test_determine_possible_moves_center_last_pos_up(self):
        board = GameBoard()
        token = Token("john", "doe")
        token.location = (4,4)
        token.last_location = (3, 4)
        possible_moves = [(5, 4), (4, 3), (4, 5)]
        self.assertEqual(possible_moves, board.determine_possible_moves(token))

if __name__ == '__main__':
    unittest.main()