from pymongo import MongoClient
from bson import  json_util
import json 
from trivial_purfuit_data_app.mongo_connector.config import config as mongo_config
client = MongoClient('mongodb+srv://' + mongo_config['username'] + ':' + mongo_config['password'] + '@' + mongo_config['host'])
db = client['trivial-purfuit-test']

def get_one_question():
    question = db.question
    one_question = question.find_one()
    return json.loads(json.dumps(one_question, default=json_util.default))
