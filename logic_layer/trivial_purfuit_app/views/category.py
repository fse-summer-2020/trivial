import requests
from flask import Blueprint, jsonify
from flask_cors import CORS, cross_origin

url = "http://127.0.0.1:5001/category"
category = Blueprint('categories', __name__, url_prefix='/category')

@category.route('/all')
def get_all_categories():
    return requests.get(url).json(), 200