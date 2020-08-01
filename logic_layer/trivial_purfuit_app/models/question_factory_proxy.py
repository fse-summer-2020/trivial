import queue
from trivial_purfuit_app.data_service.data_layer_service import get_all_categories
from trivial_purfuit_app.models.question_factory import QuestionFactory

class QuestionFactoryProxy():

    def __init__(self):
        categories = get_all_categories()
        self.factories = dict()
        for category in categories:
            cateogry_id = category["_id"]["$oid"]
            self.factories[cateogry_id] = QuestionFactory(cateogry_id)

    def get_question(self, category_id):
        return self.factories[category_id].get_random_question()
        