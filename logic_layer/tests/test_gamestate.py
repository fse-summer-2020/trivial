import unittest
from trivial_purfuit_app.gamestate import GameState

class GameState_Test(unittest.TestCase):

    # just seeing format of the dictionary
    def test_get_class_dictionary(self):
        #state = GameState()
        #state.current_round = 1
        #print(state.get_class_dict())
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()