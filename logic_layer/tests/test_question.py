import unittest
from trivial_purfuit_app.models.question import Question

class Question_Test(unittest.TestCase):

    def setUp(self):
        self.question = Question("is your team name 'No Trivial Matter", ["Yes", "No"], "Yes")

    def test_correct_answer_true(self):
        self.assertTrue(self.question.validate_answer("Yes"))

    def test_correct_answer_false(self):
        self.assertFalse(self.question.validate_answer("No"))