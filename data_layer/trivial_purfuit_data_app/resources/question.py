from flask_restful import Resource, request
from trivial_purfuit_data_app.mongo_connector.mongo import get_questions_by_category, get_all_questions, save_questions
from flask import jsonify
class Question(Resource):
    
    def get(self):
        args = request.args
        if "category_id" in args:
            category_id = args["category_id"]
            return get_questions_by_category(category_id)
        else:
            return get_all_questions()
    def post(self):
        return jsonify(save_questions(request.get_json(force=True)["questions"]))
        