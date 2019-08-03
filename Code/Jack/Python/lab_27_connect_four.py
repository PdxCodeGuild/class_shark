class Player():
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Game(object):
    """docstring for Game."""

    def __init__(self, l_players):
        self.board = [['' for i in range(6)] for i in range(7)]
        self.players = {player.color: player.name for player in l_players} or None
        self.win_patterns = {'vert': [[i][j-1], [i][j+1]],
                             'horz': [[i-1][j], [i+1][j]],
                             'ldiag': [[i-1][j-1], [i+1][j+1]],
                             'rdiag': [[i-1][j+1], [i+1][j-1]],
                            }

    def get_height(self, position):
        if self.board[position][0] != '':
            return None
        elif self.board[position][5] == '':
            return 5
        else:
            for i in range(1, 5):
                if self.board[position][i] != '':
                    return i-1

    def move(self, player, position):
        space = get_height(position)
        if space:
            self.board[position][space] = player.color
            self.moves.update((position+space), player.color)
        else:
            print('That position is filled')

    def calc_winner(self):
        count = 0
        for i in range(7):
            for j in range(5, -1, -1):
                pos = self.board[i][j]
                if pos != '':
                    if self.board[i][j-1] == pos:
                    	return self.vert_serch(i,j, pos)

    def vert_search(self, i, j, pos):
    	count = 0
    	while self.board[i][j] == pos:
    		count += 1
    		j -= 1


    def is_full(self):
        for col in self.board:
            temp = set(col)
            if '' in temp:
                return False
            else:
                return True

    def is_game_over(self):
        if calc_winner():
            pass
