import unittest
from Farkle.src.FarkleGame import FarkleGame, GameState
import Farkle.src.FarkleRoll as FarkleRoll


class FarkleRollTest(unittest.TestCase):
    def testGenerateRolls(self):
        self.assertEqual(len(FarkleRoll.FarkleRoll.all_rolls), 6**6)


class RollTest(unittest.TestCase):
    def setUp(self, **kwargs):
        self.instance = FarkleGame()

    @staticmethod
    def set_up_roll(**kwargs):
        arguments = ["one", "two", "three", "four", "five", "six"]
        return {index+1: kwargs.get(arguments[index], 0) for index in range(6)}

    def testOptionsOneRoll(self):
        roll = self.set_up_roll(one=1)
        self.instance.current_roll = roll
        self._state = GameState.DICE_ROLL
        self.instance.get_options()