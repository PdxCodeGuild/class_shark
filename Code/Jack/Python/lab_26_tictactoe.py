class Player(object):
    """docstring for Player."""

    def __init__(self, name='Default', token='X'):
        self.name = name
        self.token = token

    def __repr__(self):
        return self.token


class Game(object):
    """docstring for Game."""

    def __init__(self):
        self.board = [[' ' for i in range(3)] for i in range(3)]
        self.board[0][2] = '_'
        self.board[0][1] = '_'
        self.board[0][0] = '_'
        self.board[1][2] = '_'
        self.board[1][1] = '_'
        self.board[1][0] = '_'

    def __repr__(self):
        s_board = ''
        for line in self.board:
            line = [str(token) for token in line]
            s_board += '|'.join(line) + '\n'
        return s_board

    def move(self, row, column, token):
        if self.board[row][column] is not Player:
            self.board[row][column] = token
            return True
        else:
            return False

    def is_full(self):
        temp = []
        for row in self.board:
            temp.append(all(row))
        return all(temp)

    def win(self):
        # diag
        if type(self.board[1][1]) is Player:
            if (self.board[0][0] == self.board[1][1] == self.board[2][2]) or \
               (self.board[0][2] == self.board[1][1] == self.board[2][0]):
               return True

        for i in range(3):
        # col
            if self.board[i][0] == self.board[i][0] == self.board[i][0]:
                return True
        # row
            if self.board[0][i] == self.board[0][1] == self.board[0][i]:
                return True
            elif self.board[1][0] == self.board[1][1] == self.board[1][2]:
            	return f'{self.board[0][0]} wins7!'
            elif self.board[2][0] == self.board[2][1] == self.board[2][2]:
            	return f'{self.board[0][0]} wins8!'
            else:
            	return False

    # def diag_search(i,j):
    #     pos = self.board[i][j]
    #     x = i
    #     y = j
    #     count = 0
    #     try:
    #         while self.board[i][j] == pos:
    #             i += 1
    #             j -= 1
    #             count += 1
    #     except IndexError:
    #         break
    #     i = x
    #     j = y
    #     if count < 2:
    #         count -= 1
    #         try:
    #             while self.board[i][j] == pos:
    #                 i -= 1
    #                 j += 1
    #                 count += 1
    #         except IndexError:
    #             break
    #     i = x
    #     j = y
    #     if count < 2:
    #         count -= 1
    #         try:
    #             while self.board[i][j] == pos:
    #                 i += 1
    #                 j += 1
    #                 count += 1
    #         except IndexError


    def is_game_over(self):
        if self.is_full() or self.win():
            print(f'{self.is_full()}, {self.win()}')
            return True
        else:
            return False


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
        turn(player1, game)
        turn(player2, game)
        while not game.is_game_over():
            for player in players:
                turn(player, game)
        print(game)
        choice = input('Again? (y/n)').strip().lower()
        if choice.startswith('n'):
            break
