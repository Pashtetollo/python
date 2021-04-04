import FruitManager
from enums import Seasons, Colors, Kinds, Order

if __name__ == '__main__':
    ATB = FruitManager.FruitManager()
    ATB.add_fruit("Banana", Seasons.SUMMER, Colors.YELLOW, 15.90, 123123, Kinds.TROPICAL)
    ATB.add_fruit("Cherry", Seasons.SPRING, Colors.RED, 9.99, 144325, Kinds.BERRY)
    ATB.add_fruit("Exotic Cucumber", Seasons.SPRING, Colors.GREEN, 0.99, 543123, Kinds.TROPICAL)
    print(ATB)
    print("AFFORDABLE:\n\n")
    print(FruitManager.output(ATB.is_affordable(10.0, Order.DESC)))
    print("RIPE:\n\n")
