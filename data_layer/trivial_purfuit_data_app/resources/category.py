from flask_restful import Resource, request
from flask import jsonify
from trivial_purfuit_data_app.mongo_connector.mongo import get_category, save_categories
class Category(Resource):

    def get(self):
        return get_category()

    def post(self):
        return jsonify(save_categories(request.get_json(force=True)["categories"]))