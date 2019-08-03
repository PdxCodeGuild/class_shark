class Player():
    '''
    Player object

    # TODO implement betting mechanic
    '''

    NAME = ''

    def __init__(self, *args):
        '''
        trying to overload init func to take player name or not

        # TODO add starting money/ points
        '''
        self.hand = []
        if args:
            self.NAME = args[0]

    def __repr__(self):
        return str(self.hand)

    def set_name(self, name):
        '''
        secondary method if init is not used for naming
        '''
        self.NAME = name

    def score(self):
        # points = 0
        # for card in self.hand:
        #     points += card.value
        # return points

        return sum([card.value for card in self.hand])

    def take_card(self, card):
        '''
        takes in card object

        # TODO add card obj type check?
        '''
        self.hand.append(card)


class Dealer(Player):
    """docstring for Dealer.
        extends player, overwrites player repr to hide first card
    """

    def __init__(self):
        super().__init__()

    def __repr__(self):
        visible_cards = ['Card(Hidden)', self.hand[1:]]
        return str(visible_cards)

    def reveal(self):
        return super().__repr__()

    def visible_score(self):
        return sum([card.value for card in self.hand[1:]])
