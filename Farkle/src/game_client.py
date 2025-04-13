from FarkleGame import FarkleGame, CashOutChoice
import FarkleRoll


def run():
    while input("Play a game? Y/N ").lower() == 'y':
        print("New Game")
        current_game = FarkleGame()

        while current_game.rounds < 10:
            # Round game loop
            print("Round:", current_game.rounds+1)
            # Roll
            options = current_game.roll_dice()
            print("Current Roll:", current_game.current_roll)
            # If none, farkled. Continue to next round
            if options is None:
                print("Farkled!")
                print(current_game.game_stats())
                continue
            for index, choice in enumerate(options, start=1):
                print(index, ".", choice, "Value:", FarkleRoll.score_roll(choice))

            option_choice = -1
            while option_choice not in (idx for idx in range(1, 1+len(options))):
                option_choice = int(input("Select an option number: "))

            current_game.submit_choice(option_choice-1)
            print(current_game.round_stats())

            cash_out_choice = -1 if current_game.round_score >= 300 else CashOutChoice.CONTINUE_ROUND.value
            while cash_out_choice not in (1, 2):
                cash_out_choice = int(input("Cash Out and move to next round - 1, or Roll Again - 2: "))
            cash_out_choice_enum = CashOutChoice.map_value_to_enum(cash_out_choice)

            current_game.cash_out(cash_out_choice_enum)
            if cash_out_choice_enum == CashOutChoice.CASH_OUT:
                print(current_game.game_stats())
        # End of game
        print(current_game.game_stats())

            
           

if __name__ == "__main__":
    run()
 