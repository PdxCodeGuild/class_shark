'''
Tic tac toe
'''

class Player:
    '''
    Player model
    '''
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __repr__(self):
        return self.token


class TicTacToe:
    '''
    Tic tac toe game
    '''
    def __init__(self):
        '''
        represent board as 3x3 list
        '''
        self.board = [[' ' for i in range(3)] 
                           for i in range(3)]

    def __repr__(self):
        '''
        formatted string representation of board
        '''
        draw_board = ''
        for line in self.board:
            line = [str(token) for token in line]
            draw_board += '|'.join(line) + '\n'
        return draw_board

    def move(self, x, y, player):
        '''
        moves player onto board if the position is unoccupied
        '''
        if type(self.board[y][x]) is Player: # position is taken
            return False
        self.board[y][x] = player
        return True

    def calc_winner(self):
        '''
        returns winner if one exists or none
        '''
        for i in range(3):
            # horizontal win
            if type(self.board[i][0]) is Player and \
                (self.board[i][0] == self.board[i][1] == self.board[i][2]):
                    return self.board[i][0]
            # vertical win
            if type(self.board[0][i]) is Player and \
                (self.board[0][i] == self.board[1][i] == self.board[2][i]):
                    return self.board[0][i]

        # diagonal wins
        if type(self.board[1][1]) is Player:
            if (self.board[0][0] == self.board[1][1] == self.board[2][2]) or \
                (self.board[0][2] == self.board[1][1] == self.board[2][0]):
                    return self.board[1][1]  

    def is_full(self):
        '''
        returns if board is filled
        '''

        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def game_over(self):
        '''
        returns true if there is a winner or the board is full
        '''
        return self.is_full() or self.calc_winner()


if __name__ == '__main__':
    positions = {
        1: (0, 0), 2: (1, 0), 3: (2, 0),
        4: (0, 1), 5: (1, 1), 6: (2, 1),
        7: (0, 2), 8: (1, 2), 9: (2, 2)
    }

    game = TicTacToe()
    players = [
        Player(input('Player one: '), 'X'), 
        Player(input('Player two: '), 'O')
    ]
    
    current_round = 1
    print(game)

    while not game.game_over():
        player = players[current_round % 2]
        while True:
            try:
                move = int(input('Move: '))
                if not (0 < move < 10):
                    raise ValueError
                x, y = positions[move]
                if game.move(x, y, player):
                    print(game)
                    current_round += 1
                    break
                else: 
                    raise ValueError
            except ValueError:
                print('Enter an unoccupied position between 1-9.')

    winner = game.calc_winner()
    if winner:
        print(f'{winner.name} wins!')
    else:
        print(f'Tie!')