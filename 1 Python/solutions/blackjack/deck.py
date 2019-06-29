'''
deck.py

Deck model
'''
from random import shuffle

class Card:
    # values = {'A':10}
    # values.update({i:i for i in range(2, 11)})
    # values.update({face: 10 for face in 'JQK'})
    # # equivalent to above
    VALUES = {'A':10, **{i:i for i in range(2, 11)}, **{face: 10 for face in 'JQK'}}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.VALUES.get(rank)

    def __repr__(self):
        return f'Card({self.rank}, {self.suit})'


class Deck:
    RANKS = ['A'] + list(range(2, 11)) + list('JQK')
    SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self):
        # self.cards = []
        # for suit in self.SUITS:
        #     for rank in self.RANKS:
        #         self.cards.append(Card(rank, suit))
        self.cards = [Card(rank, suit) for suit in self.SUITS for rank in self.RANKS]

    def __str__(self):
        return str(self.cards)

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index]

    def shuffle(self):
        shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


if __name__ == '__main__':
    deck = Deck()
    print(deck)
    print(deck.draw())
    print(len(deck))
    deck.shuffle()
    print(deck)
    print(deck.draw())
    print(len(deck))
    print(deck[-1])