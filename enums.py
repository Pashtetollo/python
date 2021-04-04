from enum import Enum


class Colors(Enum):
    RED = 1
    BLACK = 2
    BLUE = 3
    YELLOW = 4
    GREEN = 5


class Kinds (Enum):
    CITRUS = 1
    BERRY = 2
    TROPICAL = 3
    MELON = 4


class Seasons (Enum):
    WINTER = 1
    SPRING = 2
    SUMMER = 3
    FALL = 4


class Order (Enum):
    ASC = 0
    DESC = 1


class Peaches (Enum):
    THICCPEACH = 1
    JUICYPEACH = 2
    INCREDIBLEPEACH = 3


class Pears (Enum):
    TASTYPEAR = 1
    BIGPEAR = 2
    KINGPEAR = 3
