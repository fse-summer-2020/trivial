from flask import Flask
from flask_restful import Api

def create_app():
    app = Flask(__name__)
    api = Api(app)
    from trivial_purfuit_data_app.resources.question import Question
    api.add_resource(Question, '/question')

    return app

    