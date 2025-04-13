from FarkleGame import FarkleGame, GameState


def run():
    while input("Play a game? Y/N ").lower() == 'y':
        print("New Game")
        current_game = FarkleGame()

        while current_game.rounds < 10:
            # roll dice
            pass

if __name__ == "__main__":
    run()
 