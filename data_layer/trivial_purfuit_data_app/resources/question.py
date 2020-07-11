from flask_restful import Resource
from trivial_purfuit_data_app.mongo_connector.mongo import get_one_question

class Question(Resource):
    
    def get(self):
        return get_one_question()