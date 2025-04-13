import unittest
from Farkle.src import FarkleRoll
from Farkle.src.DiceRoll import DiceRoll
import parameterized


class FarkleRollTest(unittest.TestCase):
    @parameterized.expand([
        (DiceRoll(one=1, two=3, five=2), 11)
    ])
    def test_valid_choices_triple_ones_fives(self, dice_roll, expected_length):
        result = FarkleRoll.valid_choices(dice_roll)
        self.assertEqual(len(result), expected_length)