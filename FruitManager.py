from Fruit import Fruit
from enums import Kinds, Seasons, Colors, Order


def func1(token):
    return token.color.value


def func2(token):
    return token.price


def output(string: []):
        stg = ""
        for i in range(len(string)):
            stg = stg + f"{i+1}:\n" + f"Name: {string[i].name}\nColor: {string[i].color.name}\n"\
                f"Season: {string[i].season.name}\nPrice: {string[i].price}\nID: {string[i].id}\n"\
                f"Fruit kind: {string[i].fruit_kind.name}\n\n"
        return stg


class FruitManager:

    def __init__(self):
        self.fruits = []

    def add_fruit(self, name: str, season: Seasons, color: Colors, price: float, id: int, fruit_kind: Kinds):
        self.fruits.append(Fruit(name, season, color, price, id, fruit_kind))

    def is_ripe(self, season: Seasons, reverse: Order = 0):
        self.fruits.sort(reverse=reverse.value, key=func2)
        ripe = []
        for i in range(len(self.fruits)):
            if self.fruits[i].season.name == season.name:
                ripe.append(self.fruits[i])
                print(f"Name: {self.fruits[i].name}\nColor: {self.fruits[i].color.name}\n"
                      f"Season: {self.fruits[i].season.name}\nPrice: {self.fruits[i].price}\n"
                      f"ID: {self.fruits[i].id}\n" f"Fruit kind: {self.fruits[i].fruit_kind.name}\n\n")
        return ripe

    def is_affordable(self, price: float, reverse: Order = 0):
        self.fruits.sort(reverse=reverse.value, key=func1)
        affordable = []
        for i in range(len(self.fruits)):
            if float(self.fruits[i].price) <= float(price):
                affordable.append(self.fruits[i])
        return affordable

    def __str__(self):
        string = ""
        for i in range(len(self.fruits)):
            string = string + f"{i+1}:\n" + f"Name: {self.fruits[i].name}\nColor: {self.fruits[i].color.name}\n"\
                f"Season: {self.fruits[i].season.name}\nPrice: {self.fruits[i].price}\nID: {self.fruits[i].id}\n"\
                f"Fruit kind: {self.fruits[i].fruit_kind.name}\n\n"
        return string
