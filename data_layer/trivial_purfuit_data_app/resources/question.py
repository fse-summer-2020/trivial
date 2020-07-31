from flask_restful import Resource
from trivial_purfuit_data_app.mongo_connector.mongo import get_questions_by_category, get_all_questions
from flask_restful import request
class Question(Resource):
    
    def get(self):
        args = request.args
        if "category_id" in args:
            category_id = args["category_id"]
            return get_questions_by_category(category_id)
        else:
            return get_all_questions()