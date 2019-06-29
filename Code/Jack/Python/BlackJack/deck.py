from random import shuffle as shuf


class Deck():
    """docstring for Deck."""

    RANK = 'A' + list(range(2, 11)) + list('JQK')
    SUIT = ['Spades', 'Diamonds', 'Clubs', 'Hearts']

    def __init__(self):
        self.cards = [Card(suit, rank)
                      for suit in self.SUIT
                      for rank in self.RANK]

    def __str__(self):
        return str(self.cards)

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
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

        self.cards = [card for card in self.card[index:index-1]]




class Card():
    """docstring for Card."""

    D_VAL = {'A': 10, **{str(i): i for i in range(2, 11)}, **{face: 10 for face in 'JQK'}}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.D_VAL[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

    def __repr__(self):
        return f'Card({self.rank}, {self.suit})'
