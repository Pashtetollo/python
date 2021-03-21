from Fruit import Fruit
from enums import Peaches


class Peach (Fruit):
    def __init__(self, kind: Peaches):
        self.kind = kind
