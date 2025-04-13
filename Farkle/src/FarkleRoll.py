from itertools import combinations_with_replacement
from Farkle.src.DiceRoll import DiceRoll
from functools import cache
from collections import defaultdict


@cache
def all_rolls() -> dict[int: set[DiceRoll]]:
    all_rolls = defaultdict(set)
    for number_of_dice in range(1, 7):
        for combo in combinations_with_replacement((1, 2, 3, 4, 5, 6), number_of_dice):
            roll = DiceRoll.fromFaceValues(combo)
            all_rolls[number_of_dice].add(roll)
    return all_rolls


@cache
def winning_rolls() -> dict[int: set[DiceRoll]]:
    winning_rolls = defaultdict(set)
    for number_of_dice in range(1, 7):
        for combo in combinations_with_replacement((1, 2, 3, 4, 5, 6), number_of_dice):
            roll = DiceRoll.fromFaceValues(combo)
            if check_roll(roll):
                winning_rolls[number_of_dice].add(roll)
    return winning_rolls


@cache
def all_winning_rolls() -> set


def triple_double(roll: DiceRoll) -> bool:
    return roll.get_roll().count(2) == 3


def straight(roll: DiceRoll) -> bool:
    return roll.get_roll().count(1) == 6
    # return all(x==1 for x in roll_tuple)


def triple_or_better(roll: DiceRoll) -> bool:
    return any(x >= 3 for x in roll.get_roll())


def one_or_five(roll: DiceRoll) -> bool:
    return bool(roll.one or roll.five)


def check_roll(roll: DiceRoll) -> bool:
    return any(func(roll) for func in [triple_double, triple_or_better, one_or_five])


def all_possible_sub_rolls(roll: DiceRoll) -> set:
    all_nums = []
    for value, count in enumerate(roll.get_roll(), start=1):
        all_nums.extend([value]*count)
    return {combinations_with_replacement(all_nums, r) for r in len(all_nums)}


def valid_choices(roll: DiceRoll):
    all_possible_combinations = all_possible_sub_rolls(roll)
    return all_possible_combinations.intersection

