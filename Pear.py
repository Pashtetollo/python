from Fruit import Fruit
from enums import Pears


class Pear (Fruit):
    def __init__(self, kind: Pears):
        self.kind = kind
