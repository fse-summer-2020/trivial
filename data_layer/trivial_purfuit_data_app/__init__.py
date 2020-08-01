from flask import Flask
from flask_restful import Api

def create_app():
    app = Flask(__name__)
    api = Api(app)
    from trivial_purfuit_data_app.resources.question import Question
    from trivial_purfuit_data_app.resources.category import Category
    api.add_resource(Question, '/question')
    api.add_resource(Category, '/category')

    return app

    