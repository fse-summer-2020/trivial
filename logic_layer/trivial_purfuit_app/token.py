class Token:
    player_name = None
    color = None
    collected_wedges = []
    location = ()
    last_location = ()
    winning_condition = False

    def __init__(self, player_name, color):
        self.player_name = player_name
        self.color = color
        pass

    def has_category_wedge(self, category):
        pass

    def has_all_wedges(self):
        return self.collected_wedges.count == 4

    def set_winning_condition(self, condition):
        self.winning_condition = condition

    def check_winning_condition(self):
        return self.winning_condition

    def add_wedge(self, wedge):
        if (wedge != None):
            self.collected_wedges.append(wedge)