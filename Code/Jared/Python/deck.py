'''
deck.py
Deck model
'''

from random import shuffle

class Card:
    # values = {'A: 10'}
    # values.update({i:i for i range(2, 11)})
    # values.update({face: 10 for face in 'JQK'})
    # equivalent to above usings **kwargs
    VALUES = {'A': 11, **{i:i for i in range(2, 11)}, **{face: 10 for face in 'JQK'}}

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.value = self.VALUES[rank]

    def __repr__(self):
        return f'Card({self.rank}, {self.suit})'


class Deck:
    RANKS = ['A'] + list(range(2, 11)) + list('JQK')
    SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spaces']
    def __init__(self):
        self.cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.cards.append(Card(rank, suit))
        # as a comprehension
        #self.cards = [Card(rank, suit) for rank in self.RANKS for suit in self.SUITS]

    def __str__(self):
        return str(self.cards)

    def __len__(self):
        return len(self.cards)

    def __getitem__(self):
        return self.cards[index]

    def shuffle(self):
        shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def cut(self, index):
        self.cards = self.cards[index:] + self.cards[:index]




if __name__ == '__main__':
    deck = Deck()
    print(deck)
    print(deck.draw())
    deck.shuffle()
    print(deck.draw())
