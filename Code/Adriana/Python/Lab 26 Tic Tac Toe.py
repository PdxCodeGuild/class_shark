#Lab 26 Tic Tac Toe
#You will write a Player class and Game class to model Tic Tac Toe,
#and a function main that models gameplay taking in user inputs through REPL.

class Player:
    def __init__(self,name,token):
        '''
        initializes a player
        '''
        self.name = name
        self.token = token

    def __repr__(self):
        return self.token

class Board:
    PIECE_X = '×'
    PIECE_O = '○'
    PIECE_EMPTY = '-'

    def __init__(self):
        self.board = [[self.PIECE_EMPTY] * 3, [self.PIECE_EMPTY] * 3, [self.PIECE_EMPTY] * 3]
        self.winner = None
        self.last_placed = None

    def __repr__(self):
        ret = ''
        for row in self.board:
            ret += '|'.join(row)
            ret += '\n'
        return ret
