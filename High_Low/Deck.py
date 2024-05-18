from collections import namedtuple
from collections.abc import Sequence
from random import randint, choice
from typing import Iterator


class Deck(Sequence):
    Card = namedtuple('Card', ['number','set'])
    sets = ['Heart', 'Club', 'Diamond', 'Spade']

    def __init__(self) -> None:
        super().__init__()
        self._cards = [self.Card(x, y) for x in range(2, 15) for y in self.sets]

    def reset(self):
        self._cards = [self.Card(x, y) for x in range(2, 15) for y in self.sets]

    def __len__(self):
        return len(self._cards)
    
    def __str__(self) -> str:
        return str([str(card) for card in self._cards])
    
    def __getitem__(self, position):
        return self._cards[position]
    
    def remove_card(self, card: Card) -> bool:
        try:
            self._cards.remove(card)
        except ValueError:
            return False
        else:
            return True
        
    def get_random_card(self) -> Card:
        result = choice(self._cards)
        return result if self.remove_card(result) else None
    

