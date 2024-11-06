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

    def scoreRollOne(self):
        roll = (1, 0, 0, 0, 0, 0)
        result = FarkleGame.score_roll(roll)
        self.assertEqual(result, 100)

    def scoreRollOnes(self):
        roll = (2, 0, 0, 0, 0, 0)
        result = FarkleGame.score_roll(roll)
        self.assertEqual(result, 200)

    def scoreRollTripleOne(self):
        roll = (3, 0, 0, 0, 0, 0)
        result = FarkleGame.score_roll(roll)
        self.assertEqual(result, 1000)

    def scoreRollMaxRoll(self):
        roll = (6, 0, 0, 0, 0, 0)
        result = FarkleGame.score_roll(roll)
        self.assertEqual(result, 4000)

    def scoreRollFive(self):
        roll = (0, 0, 0, 0, 1, 0)
        result = FarkleRoll.score_roll(roll)
        self.assertEqual(result, 50)

    def scoreRollOneFive(self):
        roll = (1, 0, 0, 0, 1, 0)
        result = FarkleGame.score_roll(roll)
        self.assertEqual(result, 150)
