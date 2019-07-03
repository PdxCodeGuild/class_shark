from random import shuffle as shuf


class Deck():
    """docstring for Deck.
        On init makes an ordered deck
        shuffle, draw, and cut

        # TODO __sub__(num_of_cards) = draw(num_of_cards) func?
    """

    RANK = 'A' + list(range(2, 11)) + list('JQK')
    SUIT = ['Spades', 'Diamonds', 'Clubs', 'Hearts']

    def __init__(self):
        '''
        creates ordered deck
        '''
        self.cards = [Card(suit, rank)
                      for suit in self.SUIT
                      for rank in self.RANK]

    def __str__(self):
        return str(self.cards)

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        '''
        useful for seeing next card
        '''
        return self.cards[index]

    def shuffle(self):
        shuf(self.cards)

    def draw(self):
        return self.cards.pop()

    def cut(self, index):
        tl_cut = []
        tl_cut.append(self.cards[index:])
        tl_cut.append(self.cards[:index])
        self.cards = tl_cut




class Card():
    """docstring for Card.

        requires suit and rank, but will calculate its own value
    """

    D_VAL = {'A': 10, **{str(i): i for i in range(2, 11)}, **{face: 10 for face in 'JQK'}}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.D_VAL[rank]

    def __str__(self):
        '''
        friendlier version for commands
        '''
        return f'{self.rank} of {self.suit}'

    def __repr__(self):
        '''
        easy display for debug
        '''
        return f'Card({self.rank}, {self.suit})'
