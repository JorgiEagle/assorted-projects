class Commentary:
    
    def shuffle_deck(self):
        return "Deck has been shuffled"
    
    def display_dealer_card(self, card):
        return f"The dealer's card is: {card}"
    
    def display_player_card(self, card):
        return f"Your card is: {card}"
    
    def display_player_choice(self, choice):
        return "You chose " + {'h': 'Higher', 'l': 'Lower'}[choice]
    
    def lose(self):
        return "You have lost"
    
    def draw(self):
        return "The cards are equal, you are still in the game"
    
    def win(self):
        return "You have won this round"
    
    def current_score(self, score):
        return f"Your current score is: {score}"
    
    def cash_out(self, options):
        return f"Would you like to cash out? {options} "

    def win_score(self, score):
        return f"You have won with a score of: {score}"
    
    def final_score(self, scores):
        return "Your final score was: " + str(sum(scores))
    
    def continue_play(self):
        return "Would you like to play? "
