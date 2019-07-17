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

    # def calc_winner(self, x, y):
    #     '''
    #     returns winner if one exists or none
    #     '''
    #     cell = self.board[y][x]
    #     if type(cell) is Player:
    #         # compare cell with n-1 cells before it and n-1 cells after
    #         for i in range(-self.n+1, self.n-1):
    #             row = True
    #             col = True
    #             ldiag = True 
    #             rdiag = True
    #             for j in range(self.n): # loop to check n in a row
    #                 if not (row or col or ldiag or rdiag):
    #                     break
    #                 # check if this is a valid x and y index and if this position == player
    #                 if row: 
    #                     row = 0 <= x+i+j < self.width and self.board[y][x+i+j] == cell
    #                 if col:
    #                     col = 0 <= y+i+j < self.height and self.board[y+i+j][x] == cell
    #                 if ldiag: 
    #                     r = y+i+j 
    #                     c = x+i+j
    #                     ldiag = 0 <= c < self.width and 0 <= r < self.height and self.board[r][c] == cell
    #                 if rdiag:
    #                     r = y+i+j 
    #                     c = x+i-j
    #                     rdiag = 0 <= c < self.width and 0 <= r < self.height and self.board[r][c] == cell

    #             if row or col or ldiag or rdiag: # if there is a match, return the winnder
    #                 self.winner = cell
    #                 return cell

    def calc_winner(self, x, y):
        '''
        recursively calculate winner from position
        '''
        directions = {
            (0,-1): (0,1), # left, right
            (-1,0): (1,0), # up, down
            (1,1): (-1,-1), # downright diagonal
            (-1,1): (1,-1), # upright diagonal
        }
        player = self.board[y][x]

        for direction in directions:
            # search for matches in direction
            matches = self.matches(player, (y, x), direction)
            if matches == self.n:
                self.winner = player
                return player
            # search in opposite direction 
            opposite_direction = self.matches(player, (y, x), directions[direction], matches)
            if opposite_direction == self.n:
                self.winner = player
                return player


    def matches(self, player, position, direction, num_matches=1):
        '''
        :player: player object
        :position: tuple of (i, j) coordinates on board
        :direction: tuple to modify position in a direction
        :num_matches: number of positions matching player

        recursively find matches from the direction of position 
        '''
        # modify position by direction
        delta = (position[0] + direction[0], position[1] + direction[1])
        # print(player, position, direction, delta, num_matches)
        i, j = delta
        if not (0 <= i < self.height and \
                0 <= j < self.width): # base case, invalid move
            return num_matches
        if self.board[i][j] != player: # base case, no match
            return num_matches

        # recursive case, keep chasing in that direction 
        return self.matches(player, delta, direction, num_matches+1)

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
    while True:
        try:
            n = int(input(f'n: ').strip())
            width = int(input(f'width: ').strip())
            height = int(input(f'height: ').strip())
            game = ConnectN(width, height, n)
            break
        except ValueError:
            print('Enter a number')

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
                move = input(f'Player {player.name}\'s move: ').strip().upper()
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