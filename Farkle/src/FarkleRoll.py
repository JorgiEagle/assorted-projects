from itertools import combinations, combinations_with_replacement, product
from Farkle.src.DiceRoll import DiceRoll
from functools import cache
from collections import defaultdict


@cache
def all_rolls() -> dict[int: list[DiceRoll]]:
    all_rolls = defaultdict(list)
    for number_of_dice in range(1, 7):
        for combo in combinations_with_replacement((1, 2, 3, 4, 5, 6), number_of_dice):
            roll = DiceRoll.fromFaceValues(combo)
            all_rolls[number_of_dice].append(roll)
    return all_rolls


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
    all_combos = [(DiceRoll.fromFaceValues(x) for x in combinations(all_nums, r)) for r in range(1, len(all_nums)+1)]
    return set().union(*all_combos)


def valid_choices(roll: DiceRoll) -> list:
    choices = []
    # one offs
    if straight(roll):
        choices.append(roll)
    if triple_double(roll):
        choices.append(roll)
    # double triples
    if roll.get_roll().count(3) == 2:
        choices.append(roll)
    # ones
    ones = [DiceRoll(one=one_count) for one_count in range(1, roll.one+1)]
    choices.extend(ones)
    # fives
    fives = [DiceRoll(five=five_count) for five_count in range(1, roll.five+1)]
    choices.extend(fives)
    # triples
    all_triples_or_higher = []
    for index, param in enumerate(roll.get_roll()):
        # skip 1 and 5
        if index in (0, 4):
            continue
        if param >= 3:
            for param_val in range(3, param+1):
                args = [0] * 6
                args[index] = param_val
                all_triples_or_higher.append(DiceRoll(*args))
    choices.extend(all_triples_or_higher)
    # one fives
    one_fives = [x+y for x, y in product(ones, fives) if sum((x+y).get_roll()) <= 6]
    choices.extend(one_fives)
    # one triples
    choices.extend(x+y for x, y in product(ones, all_triples_or_higher) if sum((x+y).get_roll()) <= 6)
    # five triples
    choices.extend(x+y for x, y in product(fives, all_triples_or_higher) if sum((x+y).get_roll()) <= 6)
    # one five triples
    choices.extend(x+y for x, y in product(one_fives, all_triples_or_higher) if sum((x+y).get_roll()) <= 6)

    return choices


def score_roll(dice_roll: DiceRoll) -> int:
    total = 0
    if straight(dice_roll):
        return 1500
    if triple_double(dice_roll):
        return 750
    if triple_or_better(dice_roll):
        for index, count in enumerate(dice_roll.get_roll(), start=1):
            if count >= 3:
                if index == 1:
                    total += 1000 * (count-2)
                else:
                    total += index * 100 * (count-2)

    # add 1s and 5s. If more than 3, will have been caught by previous
    # ones
    if dice_roll.one < 3:
        total += 100 * dice_roll.one
    # fives
    if dice_roll.five < 3:
        total += 50 * dice_roll.five
    return total
