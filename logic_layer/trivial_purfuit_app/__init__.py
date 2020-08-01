from flask import Flask
from flask_cors import CORS
def create_app():
    app = Flask(__name__)
    cors = CORS(app, resources={r"*": {"origins": "*"}})


    from trivial_purfuit_app.views.questions import questions
    app.register_blueprint(questions)
    from trivial_purfuit_app.views.logic import logic
    app.register_blueprint(logic)
    from trivial_purfuit_app.views.dice import roll
    app.register_blueprint(roll)
    
    return app

    