from FarkleGame import FarkleGame, GameState


def run():
    while input("Play a game? Y/N ").lower() == 'y':
        print("New Game")
        current_game = FarkleGame()

        while current_game.rounds < 10:
            # roll dice
            current_game.roll_dice()
            print("Your roll is:")
            print(FarkleGame.roll_to_str(current_game.current_roll))
            if current_game._state == 1:
                print("Farkled")
            else:
                print("Your possible options are:")
                for index, option in enumerate(current_game.possible_options):
                    print(f'{index+1}. {FarkleGame.roll_to_str(option)}')
                    print(f"Score: {FarkleGame.score_roll(option)}\n")
                while True:
                    try:
                        user_choice = int(input("Select an option: "))
                        if user_choice < 1 or user_choice > len(current_game.possible_options):
                            raise IndexError
                    except IndexError:
                        print(f"Invalid option, please pick between 1 and {len(current_game.possible_options)}")
                        continue
                    else:
                        break
                current_game.submit_choice(user_choice-1)
                print(current_game.round_stats())
                if current_game._state == GameState.ROUND_START:
                    continue

                while True:
                    try:
                        cash_out_choice = int(input("Cash out or continue?\n\tCash out: 1\n\tContinue: 2\n"))
                        if cash_out_choice not in [1, 2]:
                            raise IndexError
                    except IndexError:
                        print("Invalid option, please pick 1 or 2")
                        continue
                    else:
                        break
                current_game.cash_out(cash_out_choice)
                print(current_game.game_stats())


if __name__ == "__main__":
    run()
 