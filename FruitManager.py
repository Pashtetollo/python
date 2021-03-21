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
        self.__fruits = []

    def add_fruit(self, name: str, season: Seasons, color: Colors, price: float, id: int, fruit_kind: Kinds):
        self.__fruits.append(Fruit(name, season, color, price, id, fruit_kind))

    def is_ripe(self, season: Seasons, reverse: Order = 0):
        self.__fruits.sort(reverse=reverse.value, key=func2)
        for i in range(len(self.__fruits)):
            if self.__fruits[i].season.name == season.name:
                print(f"Name: {self.__fruits[i].name}\nColor: {self.__fruits[i].color.name}\n" 
                      f"Season: {self.__fruits[i].season.name}\nPrice: {self.__fruits[i].price}\n"
                      f"ID: {self.__fruits[i].id}\n" f"Fruit kind: {self.__fruits[i].fruit_kind.name}\n\n")

    def is_affordable(self, price: float, reverse: Order = 0):
        self.__fruits.sort(reverse=reverse.value, key=func1)
        affordable = []
        for i in range(len(self.__fruits)):
            if float(self.__fruits[i].price) <= float(price):
                affordable.append(self.__fruits[i])
        return affordable

    def __str__(self):
        string = ""
        for i in range(len(self.__fruits)):
            string = string + f"{i+1}:\n" + f"Name: {self.__fruits[i].name}\nColor: {self.__fruits[i].color.name}\n"\
                f"Season: {self.__fruits[i].season.name}\nPrice: {self.__fruits[i].price}\nID: {self.__fruits[i].id}\n"\
                f"Fruit kind: {self.__fruits[i].fruit_kind.name}\n\n"
        return string
