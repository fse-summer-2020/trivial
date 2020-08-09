import json

class Category(object):
    
    def __init__(self, name, category_id, color):
        self.name = name
        self.category_id = category_id
        self.color = color
    
    def get_dict(self):
        obj = dict()
        obj["name"] = self.name
        obj["category_id"] = self.category_id
        obj["color"] = self.color
        return obj
        