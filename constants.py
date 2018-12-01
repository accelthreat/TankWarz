from enum import Enum
from enum import IntEnum

class Game(IntEnum):
    WIDTH = 1280
    HEIGHT = 700
class Direction(IntEnum):
    FORWARD = 1
    BACKWARD = -1
    RIGHT = 1
    LEFT = -1
class Color(Enum):
    BLACK = "Black"
    BLUE = "Blue"
    GREEN = "Green"
    RED = "Red"
    BEIGE = "Beige"
    
    def from_int(c):
        return ColorInt[c]

ColorInt = {1 : Color.BLACK,
        2 : Color.BLUE,
        3 : Color.GREEN,
        4 : Color.RED,
        5 : Color.BEIGE}
        
class Coll_Type(IntEnum):
    TANK = 1
    PROJECTILE = 2
    ENVIRONMENT = 3


