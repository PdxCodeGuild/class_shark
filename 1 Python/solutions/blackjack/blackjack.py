# blackjack.py
from player import *
from deck import Deck

class Game:
    '''
    Represents a game of blackjack
    '''
    def __init__(self, num_players=1, cut=26):
        '''
        Initializes game with dealer, list of players, and a shuffled and cut deck
        '''
        self.dealer = Dealer()
        self.players = [Player() for i in range(num_players)]
        self.deck = Deck()
        self.deck.shuffle()
        self.deck.cut(cut)

    def play(self):
        '''
        Plays a single game of blackjack
        '''
        # deal players two cards each
        self.dealer.add(self.deck.draw())
        self.dealer.add(self.deck.draw())
        for player in self.players:
            player.add(self.deck.draw())
            player.add(self.deck.draw())

        # loop game while players are not all busted or staying
        for i, player in enumerate(self.players):
            while not player.stay and not player.busted:
                self.display(player, f'Player {i+1}') 
                while True: # prompt user to hit/stay
                    cmd = input('(h)it or (s)tay: ').lower().strip()
                    if cmd in ['h', 'hit', 's', 'stay']:
                        break
                if cmd.startswith('h'):
                    # draw card to player's hand and check if blackjack/busted
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

        # once all players are busted/staying, reveal the dealer's hand and calculate winners
        print('*'*60)
        print('Game over')
        print('*'*60)
        print("Dealer's hand: ")
        print(self.dealer.reveal())
        print(self.dealer.score())
        wins = {}

        for i, player in enumerate(self.players):
            name = f'Player {i+1}'
            self.display(player, name)
            wins[name] = self.calc_winner(player)
            print(wins[name], 'wins!')

        return wins # return dictionary of player:winner to keep track of score

    def display(self, player, name):
        '''
        Displays player's hand and score
        '''
        print('-'*60)
        print(f"{name}'s hand:")
        print(player)

        if type(player) is Dealer:
            print(player.visible_score())
        else:
            print(player.score())

    def calc_winner(self, player):
        '''
        Returns 'Player', 'House', or 'Tie' as winner.
        '''
        pscore = player.score()
        dscore = self.dealer.score()
        if (pscore >= dscore or self.dealer.busted) and not player.busted:
            return 'Player'
        elif pscore == dscore:
            return 'Tie'
        else:
            return 'House'  


if __name__ == '__main__':
    loop = True

    while True:
        try:
            num_players = int(input('Enter number of players: '))
            if not (0 < num_players < 6):
                raise ValueError
        except ValueError:
            print('Enter a real number between 1 and 5 :(((((((')
        else:
            break

    wins = {f'Player {i+1}': [] for i in range(num_players)}

    while loop:
        while True:
            try:
                cut = int(input('Cut the deck: '))
                if not (0 < cut < 53):
                    raise ValueError
            except ValueError:
                print('Enter a number between 1 and 52')            
            else:
                break

        game = Game(num_players, cut-1)
        game_round = game.play()
        wins = {k: wins[k] + [game_round[k]] for i, k in enumerate(game_round)}

        while True:
            again = input('Do you want to play again: ').strip().lower()
            if again in ['yes', 'y', 'no', 'n']:
                break

        loop = again.startswith('y')


    # print final scores of players at the end
    print('*'*60)
    print('Final score:')
    print('*'*60)
    for player in wins:
        print(player.ljust(15), *wins[player], sep='\t')
    print('*'*60)
    print('Goodbye!')