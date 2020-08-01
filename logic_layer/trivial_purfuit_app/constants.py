from enum import Enum

class State(Enum):
    ROLL_DIE = 'ROLL_DIE'
    MOVE_DIRECTION = 'MOVE_DIRECTION'
    ANSWER_TRIVIA = 'ANSWER_TRIVIA'
    POLL_CATEGORY_ALL = 'POLL_CATEGORY_ALL'
    POLL_CATEGORY_CURRENT = 'POLL_CATEGORY_CURRENT'
    GAME_END = 'GAME_END'

class SquareType(Enum):
    HEADQUARTER = 'HeadquarterSquare'
    ROLL_AGAIN_SQUARE = 'RollAgainSquare'
    HUB = 'HubSquare'
    CATEGORY = 'CategorySquare'