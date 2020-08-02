class Token:
    player_name = None
    color = None
    collected_wedges = []
    location = (4,4)
    last_location = (4,4)
    winning_condition = False

    def __init__(self, player_name, color):
        self.player_name = player_name
        self.color = color

    def has_category_wedge(self, category):
        if category in self.collected_wedges:
            return True
        else:
            return False

    def has_all_wedges(self):
        return self.collected_wedges.count == 4

    def set_winning_condition(self, condition):
        self.winning_condition = condition

    def check_winning_condition(self):
        return self.winning_condition

    def add_wedge(self, wedge):
        if (wedge != None and not self.has_category_wedge(wedge.category)):
            self.collected_wedges.append(wedge)
        else:
            raise Exception("Wedge is undefined")
    
    def get_dict(self):
        obj = dict()
        obj["player_name"]= self.player_name
        obj["color"]= self.color
        obj["collected_wedges"]= self.collected_wedges
        obj["location"]= self.location
        obj["winning_condition"]= self.winning_condition
        return obj
