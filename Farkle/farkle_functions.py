import random


def three_pairs_bool(dice_list) -> bool:
    occurrences = [dice_list.count(x) for x in range(1, 7)]
    return occurrences.count(2) == 3


def straight_bool(dice_list) -> bool:
    occurrences = [dice_list.count(x) for x in range(1, 7)]
    return occurrences.count(1) == 6


def farkled(dice_list) -> bool:
    counts = {x: dice_list.count(x) for x in range(1, 7)}
    three_occurrences = [1 for x in counts.keys() if counts[x] >= 3]
    return counts[1] == 0 and counts[5] == 0 and not three_pairs_bool(dice_list) and not straight_bool(dice_list) and not three_occurrences


def remove_multiple_from_list(the_list, value):
    return [x for x in the_list if x != value]


def remove_from_list(roll, value):
    roll.remove(value)
    return roll, 100 if value == 1 else 50
