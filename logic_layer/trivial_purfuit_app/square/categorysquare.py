from .triviasquare import TriviaSquare

class CategorySquare(TriviaSquare):
    category = None

    def __init__(self, category):
        self.category = category