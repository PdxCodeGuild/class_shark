'''
deck.py

Deck and Card models
'''
from random import shuffle

class Card:
    '''
    Represents a poker card
    '''
    # values = {'A':10}
    # values.update({i:i for i in range(2, 11)})
    # values.update({face: 10 for face in 'JQK'})

    # # equivalent to above
    VALUES = {'A':11, **{i:i for i in range(2, 11)}, **{face: 10 for face in 'JQK'}}

    def __init__(self, rank, suit):
        '''
        Initializes card with rank, suit, and computed value
        '''
        self.rank = rank
        self.suit = suit
        self.value = self.VALUES.get(rank)

    def __repr__(self):
        '''
        Returns string representation of card
        '''
        return f'Card({self.rank}, {self.suit})'


class Deck:
    '''
    Represents a deck of poker cards
    '''
    RANKS = ['A'] + list(range(2, 11)) + list('JQK')
    SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self):
        '''
        Initializes deck with 52 cards
        '''
        # self.cards = []
        # for suit in self.SUITS: # loops 4x
        #     for rank in self.RANKS: # loops 4 * 13 = 52x
        #         self.cards.append(Card(rank, suit))
        self.cards = [Card(rank, suit) for suit in self.SUITS for rank in self.RANKS]

    def __str__(self):
        '''
        Returns string representation of deck
        '''
        return str(self.cards)

    def __len__(self):
        '''
        Returns length of deck as length of cards
        '''
        return len(self.cards)

    def __getitem__(self, index):
        '''
        Returns card at index
        '''
        return self.cards[index]

    def shuffle(self):
        '''
        Shuffles cards in place
        '''
        shuffle(self.cards)

    def draw(self):
        '''
        Removes card from top of deck and returns it
        '''
        return self.cards.pop()

    def cut(self, index):
        '''
        Cuts cards at index
        '''
        self.cards = self.cards[index:] + self.cards[:index]
                     # move top         to          bottom

if __name__ == '__main__':
    # tests
    deck = Deck()
    print(deck)
    print(deck.draw())
    print(len(deck))
    deck.shuffle()
    print(deck)
    print(deck.draw())
    print(len(deck))
    print(deck[-1])