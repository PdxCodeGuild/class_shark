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
        '''
        Initializes player with empty hand list
        '''
        self.hand = []
        self.stay = False
        self.busted = False

    def __repr__(self):
        '''
        Returns string representation of hand
        '''
        return str(self.hand)

    def score(self):
        '''
        Returns sum of card values in hand
        Starts out with ace high. If busted, reduce ace to low as need.
        '''
        points = 0
        aces = 0
        for card in self.hand:
            if card.rank == 'A':
                aces += 1
            points += card.value 

        for ace in range(aces):
            if points > 21:
                points -= 10
            else:
                break
        return points

        # return sum([card.value for card in self.hand])

    def add(self, card):
        '''
        Adds card to hand
        '''
        self.hand.append(card)


class Dealer(Player):
    '''
    Represents the dealer in blackjack
    Extends the player class but keeps the first card in its hand hidden
    '''

    def __init__(self):
        '''
        Initializes dealer with empty hand
        '''
        super().__init__()

    def __repr__(self):
        '''
        Returns string representation of hand with the first card hidden
        '''
        visible_cards = [Card('Hidden', 'Hidden'), self.hand[1:]]
        return str(visible_cards)        

    def reveal(self):
        '''
        Calls superclass's __repr__() to show all cards in hand
        '''
        return super().__repr__()

    def visible_score(self):
        '''
        Returns sum of all visible cards in hand
        '''
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