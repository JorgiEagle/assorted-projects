# program to calculate probabilities of FARKLE games and outcomes and optimise strategy
# print('For ' + str(number_of_games*10) + ' rolls, ' + str(farkle_total) + ' farkles occurred, ' + str(round(((farkle_total*10)/number_of_games), 2)) + '%')
import random


def three_pairs_bool(dice_list) -> bool:
    return dice.count(2) == 3


def straight_bool(dice_list) -> bool:
    return dice.count(1) == 6


def farkled(dice_list) -> bool:
    counts = {x: dice_list.count(x) for x in range(1, 7)}
    three_occurrences = [1 for x in counts.keys() if counts[x] >= 3]
    return counts[1] == 0 and counts[5] == 0 and not three_pairs_bool(dice_list) and not straight_bool(dice_list) and not three_occurrences


def remove_from_list(the_list, value):
    return [x for x in the_list if x != value]


dice = [1, 2, 3, 4, 5, 6]
test = 1
with open('game_results_full_game' + str(test) + '.txt', 'w') as results_file:
    running_score = 0
    number_of_games = 10
    results_file.write('Strategy: Take straights and three pair, all 3 of a kind or higher, one one and only then one 5, quit under 3 dice')
    # farkle_total = 0
    # play the given number of games
    for games in range(number_of_games):
        results_file.write('Game: ' + str(games+1))
        #score for this game
        game_score = 0
        # play 10 rounds
        for game_round in range(10):
            results_file.write('\n\tRound: ' + str(game_round+1))
            round_score = 0
            # number of dice available at the start of the round is 6
            dice_left = 6
            # main control loop for round
            while True:
                # calculate roll based on number of dice left
                roll = [random.randint(1, 6) for x in range(dice_left)]
                # if farkled, set to true and exit loop, giving a score of zero
                results_file.write('\n\t\tRoll: ' + str(roll))
                if farkled(roll):
                    results_file.write('\n\t\tFARKLED')
                    round_score = 0
                    break
                # straight achieved
                if straight_bool(roll):
                    round_score += 1500
                    results_file.write('\n\t\tSTRAIGHT')
                    # new roll
                    continue
                # three two paris achieved
                if three_pairs_bool(roll):
                    results_file.write('\n\t\tThree Pair')
                    round_score += 750
                    # new roll
                    continue
                # three or more of a kind
                three_or_more = {x: roll.count(x) for x in range(1, 7) if roll.count(x) >= 3}
                if three_or_more:
                    results_file.write('\n\t\tThree of a kind: ' + str(three_or_more))
                for dice_value in three_or_more.keys():
                    round_score += dice_value*100*(three_or_more[dice_value]-2)
                    roll = remove_from_list(roll, dice_value)

                if 1 in roll:
                    roll.remove(1)
                    results_file.write('\n\t\tRemoved 1')
                    round_score += 100
                    # roll again
                elif 5 in roll:
                    results_file.write('\n\t\tRemoved 5')
                    roll.remove(5)
                    round_score += 50

                dice_left = len(roll)
                results_file.write('\n\t\tDice left = ' + str(dice_left) + '\n\t\tCurrent round score = ' + str(round_score))
                if dice_left == 0:
                    dice_left = 6

                if round_score >= 300 and dice_left < 3:
                    results_file.write('\n\t\tCash In')
                    break
                # else continue
            results_file.write('\n\tRound score: ' + str(round_score))
            game_score += round_score
        results_file.write('\nGame Score: ' + str(game_score))
        running_score += game_score
    results_file.write('\nAverage Game score = ' + str(running_score/number_of_games) + '\n')






