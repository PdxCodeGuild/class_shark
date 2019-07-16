'''
Connect n

Get n in a row to win
'''
from string import ascii_uppercase as y_coord

class Player:
    '''
    Player model
    '''
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __repr__(self):
        return self.token


class ConnectN:
    '''
    Tic tac toe game
    '''
    def __init__(self, width=8, height=8, n=3):
        '''
        represent board as 3x3 list
        '''
        self.width = width 
        self.height = height
        self.n = n
        self.winner = None
        self.board = [[' ' for i in range(width)] 
                           for j in range(height)]
        # self.board = [[str(j*i+i) for i in range(width)] 
        #                    for j in range(height)]

    def __repr__(self):
        '''
        formatted string representation of board
        '''
        # draw_board = ''
        # for i, line in enumerate(self.board):
        #     line = [str(i+1).zfill(2)] + [str(token) for token in line]
        #     draw_board += '|'.join(line) + '|\n'
        
        # draw_board += '  |' + '|'.join([y_coord[i] for i in range(self.width)]) + '|\n'
        draw_board = ''
        for i, line in enumerate(self.board):
            line = [y_coord[i]] + [str(token) for token in line]
            draw_board += '|'.join(line) + '|\n'
        
        draw_board += ' |' + '|'.join([str(i//10) for i in range(1, self.width+1)]) + '|\n'
        draw_board += ' |' + '|'.join([str(i%10) for i in range(1, self.width+1)]) + '|\n'

        return draw_board

    def move(self, x, y, player):
        '''
        moves player onto board if the position is unoccupied
        '''
        if type(self.board[y][x]) is Player: # position is taken
            return False
        self.board[y][x] = player
        self.calc_winner(x, y)
        return True

    def calc_winner(self, x, y):
        '''
        returns winner if one exists or none
        '''
        cell = self.board[y][x]
        if type(cell) is Player:
            for i in range(-self.n+1, self.n):
                row = True
                col = True
                ldiag = True 
                rdiag = True
                for j in range(self.n):
                    if not (row or col or ldiag or rdiag):
                        break
                    if row:
                        row = 0 <= x+i+j < self.width and self.board[y][x+i+j] == cell
                    if col:
                        col = 0 <= y+i+j < self.height and self.board[y+i+j][x] == cell
                    if ldiag:
                        r = y+i+j 
                        c = x+i+j
                        ldiag = 0 <= c < self.width and 0 <= r < self.height and self.board[r][c] == cell
                    if rdiag:
                        r = y+i+j 
                        c = x+i-j
                        rdiag = 0 <= c < self.width and 0 <= r < self.height and self.board[r][c] == cell

                if row or col or ldiag or rdiag:
                    self.winner = cell
                    return cell

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
        return self.is_full() or self.winner


if __name__ == '__main__':
    game = ConnectN()
    print(game)
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
                move = input('Move: ').strip().upper()
                x = int(move[1:]) - 1
                y = move[0]
                if not (0 <= x < game.width) or y not in y_coord[:game.width]:
                    raise ValueError
                y = y_coord.find(y)
                if game.move(x, y, player):
                    print(game)
                    current_round += 1
                    break
                else: 
                    raise ValueError
            except ValueError:
                print('Enter a valid unoccupied position')

    winner = game.winner
    if winner:
        print(f'{winner.name} wins!')
    else:
        print(f'Tie!')