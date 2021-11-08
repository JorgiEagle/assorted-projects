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


def acceptable_selection(user_selection) -> bool:
    # number of occurrences of each number in the user selection
    occurrences = {x: user_selection.count(x) for x in range(1, 7)}
    # Validating if the users selection meets the minimum requirements to bank and roll again
    minimum_for_valid_roll = occurrences[1] > 0 or occurrences[5] > 0 or max(occurrences.values()) >= 3
    # numbers that cannot be on their own, must be part of a three or more, unless in a straight or 3 pair
    invalid_selection_numbers = [2, 3, 4, 6]
    valid_selection = all([not(0 < occurrences[x] < 3) for x in invalid_selection_numbers])
    return minimum_for_valid_roll and (valid_selection or straight_bool(user_selection)
                                       or three_pairs_bool(user_selection))
