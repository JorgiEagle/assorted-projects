from Deck import Deck
from CommandLineCommentary import CommandLineCommentary
from Commentary import Commentary

class HighLow:
    def __init__(self, commentary_class: Commentary) -> None:
        self.deck = Deck()
        self.commentary = commentary_class

    def get_player_choice():
        pass
    
    def game(self):
        pass

    def round(self, deck):
        dealer_card = deck.get_random_card()
        player_card = deck.get_random_card()
        self.commentary.display_dealer_card()
        if dealer_card.number == 2:
            player_choice = 'h'
        elif dealer_card.number == 14:
            player_choice = 'l'
        else:
            player_choice = get_player_choice()
        print(f"Your card was: {player_card}")
        print("You chose " + {'h': 'Higher', 'l': 'Lower'}[player_choice])

        results = (player_card.number < dealer_card.number, player_card.number > dealer_card.number)

        if results[player_choice == 'l']:
            print("You have lost")
            return score
        elif player_card.number == dealer_card.number:
            print("The cards are equal, you are still in the game")
        else:
            score += 1
            print("You have won this round")

        print(f"Your current score is: {score}")
        play = input("Would you like to cash out? Y/N ")

def validate_choice(choice):
    if choice.lower() in "hl":
        return choice.lower()
    else:
        raise ValueError("Not an valid choice, must be H or L")
    
def play_game(deck: Deck):
    score = 0
    play = ''
    while play.lower() != 'y':
        if len(deck) < 42:
            deck.reset()
            print("Deck has been shuffled")
        

    print(f"You have won with a score of: {score}")
    return score

def main():
    scores = []
    deck = Deck()
    HighLow(CommandLineCommentary())

    while input("Would you like to play? ").lower() == 'y':
        result = play_game(deck)
        scores.append(result)
    
    print("Your final score was:", sum(scores))



if __name__ == "__main__":
    main()