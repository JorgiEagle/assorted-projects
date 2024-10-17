import unittest
from src.FarkleGame import FarkleGame


class RollTest(unittest.TestCase):

    def setup(self):
        self.instance = FarkleGame()

    @staticmethod
    def set_up_roll(**kwargs):
        arguments = ["one", "two", "three", "four", "five", "six"]
        return {index+1: kwargs.get(arguments[index], 0) for index in range(6)}

    def testOneRoll(self):
        roll = self.set_up_roll(one=1)
        print(roll)


RollTest.testOneRoll()