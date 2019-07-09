class Player(object):
    """docstring for Player."""

    def __init__(self, name='Default', token='X'):
        self.name = name
        self.token = token


class Game(object):
    """docstring for Game."""

    def __init__(self):
        self.board = [['' for i in range(3)] for i in range(3)]

    def __str__(self):
        s_board = ''
        for line in self.board:
            s_board += '|'.join(line) + '\n'
        return s_board

    def move(self, row, column, token):
        while True:
            if not self.board[row][column]:
                self.board[row][column] = token
                return True
            else:
                return False

    def is_full(self):
        return all(self.board)


def turn(player, game):
    loop = True
    while loop:
        print(game)
        try:
            row = int(input('Row: ').strip())
            col = int(input('Col: ').strip())
        except ValueError:
            print('Invalid Input: ')
        move_is_valid = game.move(row, col, player.token)
        if move_is_valid:
            loop = False
        else:
            print('Space is occupied')

if __name__ == '__main__':
    loop = True
    while loop:
        player1 = Player('Player1', 'X')
        player2 = Player('Player2', 'O')
        players = [player1, player2]
        game = Game()
        while game.is_full():
            for player in players:
                turn(player, game)
        choice = input('Again? (y/n)').strip().lower()
        if choice.startswith('n'):
            break
