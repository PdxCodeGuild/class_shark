# blackjack.py
from player import *
from deck import Deck

class Game:
    '''
    Represents a game of blackjack
    '''
    def __init__(self, num_players=1, cut=26):
        self.dealer = Dealer()
        self.players = [Player() for i in range(num_players)]
        self.deck = Deck()
        self.deck.shuffle()
        self.deck.cut(cut)

    def play(self):
        # initial deal
        self.dealer.add(self.deck.draw())
        self.dealer.add(self.deck.draw())

        for player in self.players:
            player.add(self.deck.draw())
            player.add(self.deck.draw())

        # loop game while players are not all busted or staying
        for i, player in enumerate(self.players):
            while not player.stay and not player.busted:
                self.display(player, f'Player {i+1}')
                while True:
                    cmd = input('(h)it or (s)tay: ').lower().strip()
                    if cmd in ['h', 'hit', 's', 'stay']:
                        break
                if cmd.startswith('h'):
                    player.add(self.deck.draw())
                    if player.score() > 21:
                        print('Busted')
                        self.display(player, f'Player {i+1}')
                        player.busted = True
                    elif player.score() == 21:
                        print('Blackjack!')
                        player.stay = True
                else:
                    player.stay = True

        while not self.dealer.stay and not self.dealer.busted:
            self.display(self.dealer, 'Dealer')
            score = self.dealer.score()
            if score < 18:
                self.dealer.add(self.deck.draw())
            elif score > 21:
                self.dealer.busted = True
            else:
                self.dealer.stay = True

        self.calc_winner()


    def display(self, player, name):
        print('-'*60)
        print(f"{name}'s hand:")
        print(player)
        if type(player) is Dealer:
            print(player.visible_score())
        else:
            print(player.score())

    def calc_winner(self):
        print('-'*60)
        print("Dealer's hand: ")
        print(self.dealer.reveal())
        print(self.dealer.score())

        for i, player in enumerate(self.players):
            self.display(player, f'Player {i+1}')
            if (player.score() >= self.dealer.score() and not player.busted) or self.dealer.busted:
                print(f'Player {i+1} wins!')
            else:
                print(f'House beats Player {i+1} :,(')


if __name__ == '__main__':
    loop = True

    while True:
        try:
            num_players = int(input('Enter number of players: '))
            if 0 < num_players < 6:
                break
            raise ValueError
        except ValueError:
            print('Enter a real number between 1 and 5 :(((((((')

    while loop:
        while True:
            try:
                cut = int(input('Cut the deck: '))
                if 0 < cut < 53:
                    break
                raise ValueError
            except ValueError:
                print('Enter a number between 1 and 52')            

        game = Game(num_players, cut-1)
        game.play()

        while True:
            again = input('Do you want to play again: ').strip().lower()
            if again in ['yes', 'y', 'no', 'n']:
                break

        loop = again.startswith('y')