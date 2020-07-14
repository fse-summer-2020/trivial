from flask import Flask

def create_app():
    app = Flask(__name__)

    from trivial_purfuit_app.views.questions import questions
    app.register_blueprint(questions)
    
    from trivial_purfuit_app.views.dice import roll
    app.register_blueprint(roll)
    
    return app

    