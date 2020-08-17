import queue
from random import randint
from trivial_purfuit_app.data_service.data_layer_service import get_questions_per_cateogry
from trivial_purfuit_app.models.question import Question

class QuestionFactory():

    def __init__(self, category):
        self.questions = QuestionFactory.get_questions(category)
        self.category = category

    @classmethod
    def get_questions(cls, category):
        questions = get_questions_per_cateogry(category)
        q = queue.PriorityQueue()
        for question in questions:
            q.put((randint(0,1000), Question(question["question"], question["possible_answers"], question["correct_answer"])))
        return q

    def get_random_question(self):
        if self.questions.empty():
            self.questions = QuestionFactory.get_questions(self.category)
        return self.questions.get()[1]
        