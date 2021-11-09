import random
from itertools import combinations_with_replacement
from itertools import product

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

def calculate_max_score(dice_roll):
    if straight_bool(dice_roll):
        return 1500
    if three_pairs_bool(dice_roll):
        return 750
    counts = {x: dice_roll.count(x) for x in range(1, 7)}
    three_occurrences = [(counts[x]-2)*x*(1000 if x == 1 else 100) for x in counts.keys() if counts[x] >= 3]
    singles = [(counts[x] * (100 if x == 1 else 50)) for x in [1, 5] if counts[x] < 3]
    return sum(three_occurrences) + sum(singles)

expected_values = dict.fromkeys(range(1,7))
probability_of_not_farkle = dict.fromkeys(range(1,7))
for K in range(1,7):
    # temp = [list(range(1, 7)) for _ in range(K)]
    dice_possibilities = list(combinations_with_replacement(range(1,7), K))
    values_of_roll = {roll : calculate_max_score(roll) for roll in dice_possibilities}
    probability_of_not_farkle_roll = sum([0 if farkled(x) else 1 for x in dice_possibilities])/len(dice_possibilities)
    probability_of_not_farkle[K] = probability_of_not_farkle_roll
    expected_score = sum(values_of_roll.values())/len(values_of_roll)
    expected_values[K] = expected_score
    
print('Expected Values for given number of dice in roll:')
for item in expected_values.items():
    print(item[0], ' ', end='')
    print('{0:.40f}'.format(item[1]))
print('Probability of not farkling for given number of dice in roll:')
for item in probability_of_not_farkle.items():
    print(item)
