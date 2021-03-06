# program to calculate probabilities of FARKLE games and outcomes and optimise strategy
# print('For ' + str(number_of_games*10) + ' rolls,' + str(farkle_total) + ' farkles occurred, ' + str(round(((farkle_total*10)/number_of_games), 2)) + '%')
import farkle_functions as ff
import random
test = 'test'
with open('game_results_game_' + str(test) + '.txt', 'w') as results_file:
    running_score = []
    number_of_games = 1
    results_file.write('Strategy: Take straights and three pair, all 3 of a kind and all ones and fives, one one and only then one 5, quit under 3 dice')
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
                if ff.farkled(roll):
                    results_file.write('\n\t\tFARKLED')
                    round_score = 0
                    break
                # straight achieved
                if ff.straight_bool(roll):
                    round_score += 1500
                    results_file.write('\n\t\tSTRAIGHT')
                    # new roll
                    continue
                # three two paris achieved
                if ff.three_pairs_bool(roll):
                    results_file.write('\n\t\tThree Pair')
                    round_score += 750
                    # new roll
                    continue
                # three or more of a kind
                three_or_more = {x: roll.count(x) for x in range(1, 7) if roll.count(x) >= 3}
                if three_or_more:
                    results_file.write('\n\t\tThree of a kind: ' + str(three_or_more))
                for dice_value in three_or_more.keys():
                    round_score += dice_value*(1000 if dice_value == 1 else 100)*(three_or_more[dice_value]-2)
                    roll = ff.remove_multiple_from_list(roll, dice_value)

                if 1 in roll:
                    if len(roll) <= 3:
                        while 1 in roll:
                            roll, to_add = ff.remove_from_list(roll, 1)
                            round_score += to_add
                    else:
                        roll, to_add = ff.remove_from_list(roll, 1)
                        round_score += to_add
                    # roll again
                elif 5 in roll:
                    if len(roll) <=3:
                        while 5 in roll:
                            roll, to_add = ff.remove_from_list(roll, 5)
                            round_score += to_add
                    else:
                        roll, to_add = ff.remove_from_list(roll, 5)
                        round_score += to_add

                dice_left = len(roll)
                results_file.write('\n\t\tDice left = ' + str(dice_left) + '\n\t\tCurrent round score = ' + str(round_score))
                if dice_left == 0:
                    dice_left = 6

                if (round_score >= 300 and dice_left < 3) or (round_score>1500 and dice_left < 4):
                    results_file.write('\n\t\tCash In')
                    break
                # else continue
            results_file.write('\n\tRound score: ' + str(round_score))
            game_score += round_score
        results_file.write('\nGame Score: ' + str(game_score) + '\n')
        running_score.append(game_score)
    final_results = '\nGames Played: ' + str(number_of_games) + '\nAverage Score: ' + \
        str(round(sum(running_score)/len(running_score))) + '\nMax Score: ' + str(max(running_score)) + '\nMin Score ' \
        + str(min(running_score))
    results_file.write(final_results)







