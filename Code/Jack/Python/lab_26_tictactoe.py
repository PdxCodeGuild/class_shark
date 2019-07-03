class Player(object):
    """docstring for Player."""

    def __init__(self, name='Default', token='X'):
        self.name = name
        self.token = token


class Game(object):
    """docstring for Game."""

    def __init__(self):
        self.board = [['' for i in range(3)] for i in range(3)]

    def __repr__(self):
        for line in self.board:
            temp = '|'.join(line)
            print(temp)
            print('-'*8)

    def move(self, row, column, token):
        while True:
            if not self.board[row][column]:
                self.board[row][column] = token
                break
            else:
                print('Invalid move')

    def is_full(self):
        return all(self.board)


def turn(player, game):
    game()
    row = input('Row: ')
    col = input('Col: ')
    game.move(row, col, player.token)

if __name__ == '__main__':
    loop = True
    while loop:
        player1 = Player('Player1', 'X')
        player2 = Player('Player2', 'O')
        game = Game()
        turn(Player1, game)
