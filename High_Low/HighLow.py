from Deck import Deck
from Commentary import Commentary
from abc import abstractmethod
class HighLow:
    def __init__(self, commentary_instance: Commentary) -> None:
        self.deck = Deck()
        self.commentary = commentary_instance
        self.scores = []

    @abstractmethod
    def get_player_input(self, message):
        pass
    

    def game(self, deck: Deck):
        play = True
        game_total = 0
        while play:
            if len(deck) < 42:
                deck.reset()
                self.commentary.shuffle_deck()
            round_result = self.round(deck)
            if round_result < 0:
                return 0
            else:
                game_total += round_result
            self.commentary.current_score(game_total)
            play = self.get_player_input(self.commentary.cash_out())
        return game_total

    def round(self, deck: Deck):
        dealer_card = deck.get_random_card()
        player_card = deck.get_random_card()
        self.commentary.display_dealer_card(dealer_card)
        if dealer_card.number == 2:
            player_choice = 'h'
        elif dealer_card.number == 14:
            player_choice = 'l'
        else:
            player_choice = self.get_player_input(self.commentary.get_player_choice())
        self.commentary.display_player_card(player_card)
        self.commentary.display_player_choice(player_choice)

        results = (player_card.number < dealer_card.number, player_card.number > dealer_card.number)

        if results[player_choice == 'l']:
            self.commentary.lose()
            return -1
        elif player_card.number == dealer_card.number:
            self.commentary.draw()
            return 0
        else:
            self.commentary.win()
            return 1


    def validate_choice(choice):
        if choice.lower() in "hl":
            return choice.lower()
        else:
            raise ValueError("Not an valid choice, must be H or L")
        

    def play(self):
        self.game(self.deck)