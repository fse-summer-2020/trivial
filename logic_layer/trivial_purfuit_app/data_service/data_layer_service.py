import requests

url = "http://127.0.0.1:5001/"

def get_questions_per_cateogry(category_id):
    return requests.get(url + "question?category_id=" + category_id).json()["questions"]

def get_all_categories():
    return requests.get(url + "category").json()["categories"]