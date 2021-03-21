from enums import Seasons, Colors, Kinds


class Fruit:

    def __init__(self):
        self.name = None
        self.season = None
        self.color = None
        self.price = None
        self.id = None
        self.fruit_kind = None

    def __init__(self, name: str, season: Seasons, color: Colors, price: float, id: int, fruit_kind: Kinds):
        self.name = name
        self.season = season
        self.color = color
        self.price = price
        self.id = id
        self.fruit_kind = fruit_kind
