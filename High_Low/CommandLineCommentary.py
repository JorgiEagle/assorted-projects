from Commentary import Commentary

def print_to_cl(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper


class CommandLineCommentary(Commentary):
    @print_to_cl
    def shuffle_deck():
        return super().shuffle_deck()
    
    @print_to_cl
    def display_dealer_card(self, card):
        return super().display_dealer_card(card)
    
    @print_to_cl
    def display_player_card(self, card):
        return super().display_player_card(card)
    
    @print_to_cl
    def display_player_choice(self, choice):
        return super().display_player_choice(choice)
    
    @print_to_cl
    def lose(self):
        return super().lose()
    
    @print_to_cl
    def draw(self):
        return super().draw()
    
    @print_to_cl
    def win(self):
        return super().win()
    
    @print_to_cl
    def current_score(self, score):
        return super().current_score(score)

    @print_to_cl
    def win_score(self, score):
        return super().win_score(score)
    
    @print_to_cl
    def final_score(self, scores):
        return super().final_score(scores)