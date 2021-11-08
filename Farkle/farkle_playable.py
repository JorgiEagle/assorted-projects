# program to calculate probabilities of FARKLE games and outcomes and optimise strategy
import random
import time
import farkle_functions as ff


while input('Do you want to play? Y/N: ').upper() == 'Y':
    print('Game Start')
    print('Please separate all numbers with a single space')
    # score for this game
    game_score = 0

    # play 10 rounds
    for game_round in range(10):
        print('Current Score: ' + str(game_score))
        print('Round ' + str(game_round+1))
        round_score = 0
        # number of dice available at the start of the round is 6
        dice_left = 6
        # main control loop for round
        while True:
            # calculate roll based on number of dice left
            print('Current Round Score: ' + str(round_score))
            print('Dice Left: ' + str(dice_left))
            print('Rolling')
            roll = [random.randint(1, 6) for x in range(dice_left)]
            print('Roll:' + str(roll))

            # if farkled, set to true and exit loop, giving a score of zero
            if ff.farkled(roll):
                print('FARKLED')
                time.sleep(3)
                round_score = 0
                break

            # list to hold users selected numbers
            user_selection = []
            roll_view = roll
            selection_finished = False

            while not selection_finished:
                accepted_input = False
                # until an accepted input is found
                while not accepted_input:
                    try:
                        # catch any non number characters
                        user_selection.extend(list(map(int, input('Make your selection: ').split())))
                    except ValueError:
                        print('Please type only numbers separated with a space')
                        continue
                    # check if the counts of each number selected aligns with those present in the roll
                    selection_in_roll = all([user_selection.count(x) <= roll_view.count(x) for x in range(1, 7)])

                    if selection_in_roll and ff.acceptable_selection(user_selection):
                        accepted_input = True
                    else:
                        print('Please enter a valid selection (1s, 5s, triplets, straight, or three two pair) which is'
                              ' a subset of your roll, separated by spaces')
                        print('Your current roll:', roll_view)

                for value in user_selection:
                    roll_view.remove(value)

                if not ff.farkled(roll_view):
                    print('Your current selection:', user_selection)
                    print('Remaining in the roll:', roll_view)
                    if input('Are you finished your selection? (Y/N): ').upper() == 'Y':
                        selection_finished = True
                else:
                    selection_finished = True

            # process user selection
            # straight achieved
            if ff.straight_bool(user_selection):
                round_score += 1500
                print('STRAIGHT, 1500 points, roll again')
                time.sleep(3)
                # new roll
                continue
            # three two paris achieved
            if ff.three_pairs_bool(user_selection):
                round_score += 750
                print('Three Pair, 750 points, roll again')
                time.sleep(3)
                # new roll
                continue
            # three or more of a kind
            three_or_more = {x: user_selection.count(x) for x in range(1, 7) if user_selection.count(x) >= 3}
            if three_or_more:
                print('Three of a kind:' + str(three_or_more.keys()))
            for dice_value in three_or_more.keys():
                round_score += dice_value*(1000 if dice_value == 1 else 100)*(three_or_more[dice_value]-2)
                roll = ff.remove_multiple_from_list(roll, dice_value)
                user_selection = ff.remove_multiple_from_list(user_selection, dice_value)

            while 1 in user_selection:
                print('1, 100 points')
                roll.remove(1)
                user_selection.remove(1)
                round_score += 100

            while 5 in user_selection:
                print('5, 50 points')
                roll.remove(5)
                user_selection.remove(5)
                round_score += 50

            if (dice_left := len(roll)) == 0:
                dice_left = 6

            print(roll)
            print('Dice left:', dice_left)
            print('Current Round Score:', round_score)
            if round_score >= 300:
                if input('Cash in or Roll again (C/R): ').upper() == 'C':
                    break
            else:
                input("Roll again (R): ")

            # else continue
        print('Round score:', str(round_score))
        game_score += round_score
    print('Game Score:', str(game_score))
