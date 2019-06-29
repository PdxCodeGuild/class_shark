class Player():

    NAME = ''

    def __init__(self):
        self.hand = []

    def __repr__(self):
        return str(self.hand)

    def set_name(self, name):
        self.NAME = name

    def score(self):
        # points = 0
        # for card in self.hand:
        #     points += card.value
        # return points

        return sum([card.value for card in self.hand])

    def add(self, card):
        self.hand.append(card)


class Dealer(Player):
    """docstring forDealer."""

    def __init__(self):
        super().__init__()

    def __repr__(self):
        visible_cards = ['Card(Hidden)', self.hand[1:]]
        return str(visible_cards)

    def reveal(self):
        return super().__repr__()

    def visible_score(self):
        return sum([card.value for card in self.hand[1:]])
