import unittest
from Fruit import Fruit
import os
import pep8
from enums import Seasons, Colors, Kinds, Order
from FruitManager import FruitManager


class TestFruitManager(unittest.TestCase):
    def setUp(self):
        self.fruitmanager = FruitManager()
        self.a = Fruit("Banana", Seasons.SUMMER, Colors.YELLOW, 15.90, 123123, Kinds.TROPICAL)
        self.b = Fruit("Exotic Cucumber", Seasons.SPRING, Colors.GREEN, 0.99, 543123, Kinds.TROPICAL)
        self.c = Fruit("Cherry", Seasons.SPRING, Colors.RED, 9.99, 144325, Kinds.BERRY)
        self.fruitmanager.fruits = [self.a, self.b, self.c]

    def test_is_ripe(self):
        self.assertEqual(self.fruitmanager.is_ripe(Seasons.SPRING, Order.ASC),
                         [self.b, self.c])

    def test_is_affordable(self):
        self.assertEqual(self.fruitmanager.is_affordable(10, Order.ASC),
                         [self.c, self.b])


class TestPep8(unittest.TestCase):
    def test_pep8(self):
        style = pep8.StyleGuide()
        style.options.max_line_length = 120
        filenames = []
        for root, _, files in os.walk('~/PycharmProjects/pythonProject'):
            if "venv" not in root:
                python_files = [f for f in files if f.endswith('.py')]
                for file in python_files:
                    filename = '{0}/{1}'.format(root, file)
                    filenames.append(filename)
        check = style.check_files(filenames)

        print(f'PEP8 style errors: {check.total_errors}')


if __name__ == '__main__':
    unittest.main()
