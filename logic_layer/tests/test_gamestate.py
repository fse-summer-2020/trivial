import unittest
import json
from trivial_purfuit_app.gamestate import GameState
from trivial_purfuit_app.token import Token
from trivial_purfuit_app.constants import State
from trivial_purfuit_app.constants import Directions
from trivial_purfuit_app.models.category import Category

class GameState_Test(unittest.TestCase):

    def setUp(self):
        self.player_one = dict()
        self.player_one["name"] = "john"
        self.player_one["color"] = "green"
        arr = []
        arr.append(self.player_one)

        #ew
        self.player_two = dict()
        self.player_two["name"] = "jane"
        self.player_two["color"] = "blue"
        arr.append(self.player_two)
        self.game_state = GameState(arr)
        
    def test_get_player_order(self):
        with self.subTest():
            self.assertEqual(self.game_state.player_order[0].player_name, self.player_one["name"])

    # just seeing format of the dictionary
    def test_get_class_dictionary(self):
        self.game_state.current_round = 1
        print(self.game_state.get_class_dict())

    def test_get_die_roll_success(self):
        self.game_state.current_state = State.ROLL_DIE
        self.game_state.get_die_roll()
        token = Token("john", "blue")
        token.location = (4,4)
        token.last_location = (3,4)
        self.game_state.current_player = token
        with self.subTest():
            self.assertGreater(self.game_state.moves_left, 0)
        with self.subTest():
            self.assertGreater(len(self.game_state.available_next_squares), 0)
        with self.subTest():
            self.assertEqual(self.game_state.current_state, State.MOVE_DIRECTION)

    def test_get_die_roll_fail(self):
        self.game_state.current_state = State.POLL_CATEGORY_ALL
        with self.assertRaises(Exception):
            self.game_state.get_die_roll()

    def test_set_category_success(self):
        self.game_state.current_state = State.POLL_CATEGORY_ALL
        cat = Category("test", "5f0b7f5190677a74898769a6", "green") # confirm this exists cat id exists if test is failing
        self.game_state.set_category(cat)
        with self.subTest():
            self.assertTrue(self.game_state.current_state == State.ANSWER_TRIVIA)
        with self.subTest():
            self.assertIsNotNone(self.game_state.current_trivia_question)

    def test_set_category_fail(self):
        self.game_state.current_state = State.ROLL_DIE
        with self.assertRaises(Exception):
            self.game_state.set_category(None)

    def test_go_to_next_player_no_wrap(self):
        self.game_state.go_to_next_player()
        self.assertEqual(self.player_two["name"], self.game_state.current_player.player_name)

    def test_go_to_next_player_wrap(self):
        self.game_state.go_to_next_player()
        self.game_state.go_to_next_player()
        self.assertEqual(self.player_one["name"], self.game_state.current_player.player_name)

    def test_answer_trivia_correct_answer_category_square(self):
        cat = Category("test", "5f0b7f5190677a74898769a6", "green") # confirm this exists cat id exists if test is failing
        self.game_state.current_state = State.POLL_CATEGORY_ALL
        self.game_state.set_category(cat)
        answer = self.game_state.current_trivia_question.correct_answer
        self.game_state.current_player.location = (5, 4)
        self.game_state.answer_trivia(answer)
        self.assertEqual(self.game_state.current_state, State.ROLL_DIE)

    def test_answer_trivia_correct_answer_hq_square(self):
        cat = Category("test", "5f0b7f5190677a74898769a6", "green") # confirm this exists cat id exists if test is failing
        self.game_state.current_state = State.POLL_CATEGORY_ALL
        self.game_state.set_category(cat)
        answer = self.game_state.current_trivia_question.correct_answer
        self.game_state.current_player.location = (4, 0)
        self.game_state.answer_trivia(answer)
        with self.subTest():
            self.assertGreater(len(self.game_state.current_player.collected_wedges), 0)
        with self.subTest():
            self.assertEqual(self.game_state.current_state, State.ROLL_DIE)

    def test_answer_trivia_correct_answer_hub_square_no_wedges(self):
        cat = Category("test", "5f0b7f5190677a74898769a6", "green") # confirm this exists cat id exists if test is failing
        self.game_state.current_state = State.POLL_CATEGORY_ALL
        self.game_state.set_category(cat)
        answer = self.game_state.current_trivia_question.correct_answer
        self.game_state.current_player.location = (4, 4)
        self.game_state.answer_trivia(answer)
        self.assertEqual(self.game_state.current_state, State.ROLL_DIE)

    def test_answer_trivia_correct_answer_hub_square_all_wedges(self):
        cat = Category("test", "5f0b7f5190677a74898769a6", "green") # confirm this exists cat id exists if test is failing
        self.game_state.current_state = State.POLL_CATEGORY_ALL
        self.game_state.set_category(cat)
        answer = self.game_state.current_trivia_question.correct_answer
        self.game_state.current_round = 2
        self.game_state.current_player.location = (4, 4)
        self.game_state.current_player.collected_wedges.extend(range(1, 5)) #hack
        self.game_state.answer_trivia(answer)
        self.assertEqual(self.game_state.current_state, State.GAME_END)

    def test_move_token_need_direction_input(self):
        self.game_state.current_player.location = self.game_state.current_player.last_location = (1, 4)
        self.game_state.moves_left = 3
        self.game_state.move_token(Directions.UP)
        self.assertEqual(self.game_state.current_state, State.MOVE_DIRECTION)

    def test_move_token_roll_again_square(self):
        self.game_state.current_player.location = self.game_state.current_player.last_location = (0, 4)
        self.game_state.moves_left = 2
        self.game_state.move_token(Directions.LEFT)
        self.assertEqual(self.game_state.current_state, State.ROLL_DIE)

    def test_move_token_hub_square(self):
        self.game_state.current_player.location = self.game_state.current_player.last_location = (3, 4)
        self.game_state.moves_left = 1
        self.game_state.move_token(Directions.DOWN)
        self.assertEqual(self.game_state.current_state, State.POLL_CATEGORY_CURRENT)

    def test_move_token_hq_or_category_square(self):
        self.game_state.current_player.location = self.game_state.current_player.last_location = (3, 4)
        self.game_state.moves_left = 1
        self.game_state.move_token(Directions.UP)
        self.assertEqual(self.game_state.current_state, State.ANSWER_TRIVIA)

if __name__ == '__main__':
    unittest.main()