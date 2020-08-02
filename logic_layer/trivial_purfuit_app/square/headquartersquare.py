from .triviasquare import TriviaSquare

class HeadquarterSquare(TriviaSquare):
    category = None

    def __init__(self, category=""):
        self.category = category