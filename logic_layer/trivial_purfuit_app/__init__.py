from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    cors = CORS(app, resources={r"*": {"origins": "*"}})

    from trivial_purfuit_app.views.utility import utility
    app.register_blueprint(utility)
    from trivial_purfuit_app.views.logic import logic
    app.register_blueprint(logic)

    
    return app

    