from pymongo import MongoClient
from bson.objectid import ObjectId
from bson import  json_util
import json 
from trivial_purfuit_data_app.mongo_connector.config import config as mongo_config
client = MongoClient('mongodb+srv://' + mongo_config['username'] + ':' + mongo_config['password'] + '@' + mongo_config['host'])
db = client['trivial-purfuit-test']

def get_questions_by_category(category_id):
    question_collection = db.question
    questions = question_collection.find({"category_id": ObjectId(category_id)})
    return json.loads(json.dumps({"questions":list(questions)}, default=json_util.default))

def get_all_questions():
    question_collection = db.question
    questions = question_collection.find({})
    return json.loads(json.dumps({"questions":list(questions)}, default=json_util.default))

def get_category():
    category_collection = db.category
    categories = category_collection.find({})
    return json.loads(json.dumps({"categories": list(categories)} , default=json_util.default))