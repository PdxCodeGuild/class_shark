class Player():
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Game(object):
    """docstring for Game."""

    HEIGHT = 6
    WIDTH = 7

    def __init__(self, l_players):
        self.board = [['' for i in range(self.WIDTH)] for i in range(self.HEIGHT)]
        self.players = {player.name: player.color for player in l_players} or None
        # self.win_patterns = {'vert': [[i][j-1], [i][j+1]],
        #                      'horz': [[i-1][j], [i+1][j]],
        #                      'ldiag': [[i-1][j-1], [i+1][j+1]],
        #                      'rdiag': [[i-1][j+1], [i+1][j-1]],
        #                     }

    def __str__(self):
        retstr = ''
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                retstr += self.board[i][j] + '|'
        return retstr
        # return [([(self.board[i][j] + '|') for j in range(self.WIDTH)] + '\n') for i in range(self.HEIGHT)]

    def get_height(self, position):
        pass
        # if self.board[position]


        # if self.board[position][0] != '':
        #     return None
        # elif self.board[position][5] == '':
        #     return 5
        # else:
        #     for i in range(1, 5):
        #         if self.board[position][i] != '':
        #             return i-1

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

    def vert_search(self, i, j, pos):
        count = 0
        while self.board[i][j] == pos:
            count += 1
            j -= 1

players = []
for i in range(2):
    name = input(f'player {i} Name: ').strip().lower()
    if i == 0:
        token = 'O'
    else:
        token = 'X'
    players.append(Player(name, token))
game = Game(players)
print(game.players)
