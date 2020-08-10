import requests

url = "http://127.0.0.1:5001/"

def get_questions_per_cateogry(category_id):
    questions = requests.get(url + "question?category_id=" + category_id).json()["questions"]
    for question in questions:
        question["_id"] = question["_id"]["$oid"]
        question["category_id"] = question["category_id"]["$oid"]
    return questions

def get_all_categories():
    categories = requests.get(url + "category").json()["categories"]
    for category in categories:
        category["_id"] = category["_id"]["$oid"]
    return categories

def save_questions(questions):
    resp = requests.post(url + "question", json={"questions": questions})
    return resp.json()

def save_categories(categories):
    resp = requests.post(url + "category", json={"categories": categories})
    return resp.json()
