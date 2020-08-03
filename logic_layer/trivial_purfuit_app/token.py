class Token:    

    def __init__(self, player_name, color):
        self.player_name = player_name
        self.color = color
        self.collected_wedges = []
        self.location = (4,4)
        self.last_location = (4,4)
        self.winning_condition = False

    def has_category_wedge(self, category):
        if category in self.collected_wedges:
            return True
        else:
            return False

    def has_all_wedges(self):
        return len(self.collected_wedges) == 4

    def set_winning_condition(self, condition):
        self.winning_condition = condition

    def check_winning_condition(self):
        return self.winning_condition

    def reset_last_location(self):
        self.last_location = self.location

    def add_wedge(self, category):
        if (category != None and not self.has_category_wedge(category)):
            self.collected_wedges.append(category)
        else:
            raise Exception("Wedge is undefined")
    
    def get_dict(self):
        obj = dict()
        obj["player_name"]= self.player_name
        obj["color"]= self.color
        obj["collected_wedges"]= [category.get_dict() for category in self.collected_wedges]
        obj["location"]= self.location
        obj["winning_condition"]= self.winning_condition
        return obj
