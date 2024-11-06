from collections import Counter
from itertools import combinations_with_replacement


class FarkleRoll:

    all_rolls = None
    winning_rolls = None

    def __update_base(combo: tuple) -> tuple[int]:
        count = {x: 0 for x in range(1, 7)}
        count.update(Counter(combo))
        return tuple(count.values())

    @classmethod
    def generate_rolls(cls):
        cls.all_rolls = {number_of_dice: [cls.__update_base(combo) for combo in
                                          combinations_with_replacement([1, 2, 3, 4, 5, 6], number_of_dice)
                                          ] for number_of_dice in range(1, 7)}
        cls.winning_rolls = {x: {roll for roll in cls.all_rolls[x] if not cls.check_roll(roll)} for x in range(1, 7)}

    def triple_double(roll_tuple) -> bool:
        return tuple(roll_tuple).count(2) == 3

    def straight(roll_tuple) -> bool:
        return roll_tuple == (1, 1, 1, 1, 1, 1)
        # return all(x==1 for x in roll_tuple)

    def triple_or_better(roll_tuple) -> bool:
        return any(x >= 3 for x in roll_tuple)

    def one_or_five(roll_tuple) -> bool:
        return roll_tuple[0] or roll_tuple[4]

    def check_roll(roll_tuple) -> bool:
        return not any(func(roll_tuple) for func in [FarkleRoll.triple_double, FarkleRoll.straight,
                                                     FarkleRoll.triple_or_better, FarkleRoll.one_or_five])


FarkleRoll.generate_rolls()