'''
players.py
Player model
'''
from deck import Deck

class Player:
    def __init__(self):
        self.hand = []
        self.stay = False
        self.busted = False

    def __repr__(self):
        return str(self.hand)

    def score(self):
        aces = 0
        points = 0
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
        # # as comprehension
        # return sum([card.value for card in self.hand])

    def add(self, card):
        self.hand.append(card)

class Dealer(Player):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        visible_cards = ['Card(Hidden)', self.hand[1:]]
        return str(visible_cards)

    def reveal(self):
        return super().__repr__()

    def visible_score(self):
        return sum(card.value for card in self.hand[1:])
    

if __name__ == '__main__':
    p = Player()
    deck = Deck()
    card = deck.draw()
    print(card)

    p.add(deck.draw())
    print(p, p.score())
