from pymongo import MongoClient
from bson.objectid import ObjectId
from bson import  json_util
import json 
from trivial_purfuit_data_app.mongo_connector.config import config as mongo_config
client = MongoClient('mongodb://localhost/')
# client = MongoClient('mongodb+srv://' + mongo_config['username'] + ':' + mongo_config['password'] + '@' + mongo_config['host'])
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

def save_questions(questions):
    question_collection = db.question
    ids = []
    for question in questions:
        if question["_id"] == "":
            question["_id"] = ObjectId()
        else:
            question["_id"] = ObjectId(question["_id"])
        question["category_id"] = ObjectId(question["category_id"])
        ids.append(question_collection.update(spec={"_id":question["_id"]},document=question, upsert=True))
    return json.loads(json.dumps({"ids":ids}, default=json_util.default))

def save_categories(categories):
    category_collection = db.category
    ids= []
    for category in categories:
        category["_id"] = ObjectId(category["_id"])
        ids.append(category_collection.update(spec={"_id":category["_id"]},document=category, upsert=True))
    return json.loads(json.dumps({"ids":ids}, default=json_util.default))
