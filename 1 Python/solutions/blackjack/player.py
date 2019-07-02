'''
player.py

Player and Dealer models for Blackjack
'''
from deck import Deck, Card

class Player:
    '''
    Represents a player in blackjack
    '''

    def __init__(self):
        self.hand = []

    def __repr__(self):
        return str(self.hand)

    def score(self):
        # points = 0
        # for card in self.hand:
        #     points += card.value 
        # return points

        return sum([card.value for card in self.hand])

    def add(self, card):
        self.hand.append(card)


class Dealer(Player):
    '''
    Represents the dealer in blackjack
    Extends the player class but keeps the first card in its hand hidden
    '''

    def __init__(self):
        super().__init__()

    def __repr__(self):
        visible_cards = [Card('Hidden', 'Hidden'), self.hand[1:]]
        return str(visible_cards)        

    def reveal(self):
        return super().__repr__()

    def visible_score(self):
        return sum([card.value for card in self.hand[1:]])


if __name__ == '__main__':
    # tests
    deck = Deck()
    deck.shuffle()
    p = Player()
    d = Dealer()
    p.add(deck.draw())
    p.add(deck.draw())
    print('Player', p, p.score())
    d.add(deck.draw())
    d.add(deck.draw())
    print('Dealer', d, d.visible_score())
    print('Dealer', d.reveal(), d.score())