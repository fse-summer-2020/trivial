class Question():

    def __init__(self, question, possible_answers, correct_answer):
        self.question = question
        self.possible_answers = possible_answers
        self.correct_answer = correct_answer

    def validate_answer(self, given_answer):
        return given_answer == self.correct_answer
    
    def get_dict(self):
        obj = dict()
        obj["question"] = self.question
        obj["possible_answers"] = self.possible_answers
        obj["correct_answer"] = self.correct_answer
        return obj