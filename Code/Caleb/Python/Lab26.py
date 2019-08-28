'''
Lab 26: Tic-Tac-Toe
Tic Tac Toe is a game. Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid. Whoever gets three in a row first wins.

You will write a Player class and Game class to model Tic Tac Toe, and a function main that models gameplay taking in user inputs through REPL.
'''


class Player(object):
    '''
    Player Class
        The Player class has the following properties:
            name = player name
            token = 'X' or 'O'
    '''

    def __init__(self, name='Player 2', token='O'):
        '''
        Initializer for the class
        '''
        self.name = name
        self.token = token
        pass

    def __repr__(self):
        if self.name == 'Player 1':
            self.name = 'Player 2'
            self.token = 'O'
        elif self.name == 'Player 2':
            self.name = 'Player 1'
            self.token = 'X'
        return self.token

class Game():
    '''
    Game Class
    The Game class has the following properties:
        board = your representation of the board
            You can represent the board however you like, such as a 2D list, tuples, or dictionary.
    '''

    def __init__(self):
        '''
        '''
        self.board = []
        for i in range(3):
            self.board.append([' ', ' ', ' '])
        print(self.board)
        self.move_counter = 0
        self.main()
        pass

    def __repr__(self):
        '''
        __repr__() Returns a pretty string representation of the game board
        '''
        for i in range(len(self.board)):
            print('|'.join(self.board[i]))
        # for i in range(len(self.board)):
        #     print(self.board[i])
        return ('TicTacToe, programmed in Python by Caleb Mealey')

    def move(self, x, y, player):
        '''
        move(x, y, player) Place a player's token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position.
        '''
        if self.is_full(x, y):
            self.board[x][y] = f'{player}'
        self.calc_winner()
        self.move_counter += 1
        pass
    
    def calc_winner(self):
        '''
        calc_winner() What token character string has won or None if no one has.
        '''
        player_1_wins = ['XXX']
        player_2_wins = ['OOO']
        self.results = []
        for i in range(3):
            for z in range(3):
                self.results.append(self.board[i][z])
        self.results_disp = []
        for i in range(3):
            self.results_disp.append([self.results[i]+ self.results[i+3]+ self.results[i+6]])
        self.results_disp.append([self.results[0]+ self.results[1]+ self.results[2]])
        self.results_disp.append([self.results[3]+ self.results[4]+ self.results[5]])
        self.results_disp.append([self.results[6]+ self.results[7]+ self.results[8]])
        self.results_disp.append([self.results[0]+ self.results[4]+ self.results[8]])
        self.results_disp.append([self.results[2]+ self.results[4]+ self.results[6]])
        # print(self.results_disp)
        game_check = False
        while not game_check:
            if player_1_wins in self.results_disp:
                print('Player 1 wins! Thanks for playing!')
                game_check = True
                break
            elif player_2_wins in self.results_disp:
                print('Player 2 wins! Thanks for playing!')
                game_check = True
                break
            else:
                break
        return game_check

    def move_input(self):
        '''
        method to get input from Player for their next move
        '''
        tf = True
        while tf:
            try:
                row = int(input(f'Enter the row (1-3) where you would like to place your token:'))
                if 0 < int(row) <= 3:
                    x = int(row)-1
                    tf = False
                    break
                else:
                    row = int(input(f'Enter the row (1-3) where you would like to place your token:'))
            except ValueError:
                print('Invalid Entry, please enter a valid number between 1-3')
        while not tf:
            try:
                column = int(input(f'Enter the column (1-3) where you would like to place your token:'))
                if 0 < int(column) <= 3:
                    y = int(column)-1
                    tf = True
                    break
            except ValueError:
                print('Invalid Entry, please enter a valid number between 1-3')
        xy = [x, y]
        return xy       

    def is_full(self, x, y):
        '''
        is_full() Returns true if the game board is full.
        '''
        check = False
        while not check:
            if self.board[x][y] == ' ':
                return True
                break
            elif self.board[x][y] == 'X' or self.board[x][y] == 'O':
                print('Invalid move, that space is already occupied')
                return False
                break

    def is_game_over(self):
        '''
        is_game_over() Returns true if the game board is full or a player has won.
        '''
        game_over = False
        if self.calc_winner() == True: 
            game_over = True
        elif self.move_counter > 8:
            game_over = True
            print('This game is a draw! Neither player has won, and there are no more available spaces to move.')
        return game_over

    def main(self):
        '''
        Main game logic
        '''
        # print(Player())
        current_player = Player()
        print('Welcome to Lab 26: Tic Tac Toe. A program coded by Caleb Mealey.')
        print('This game is designed to be a two player game of the classic TicTacToe we all know and love.')
        print('Starting with \'Player 1\' we will begin!')
        print(self)
        game_live = True
        while game_live:
        # self.move_input()
            xy = (self.move_input())
            self.move(xy[0], xy[1], current_player)
            if current_player == 'X':
                current_player = 'O'
            elif current_player == 'O':
                current_player = 'X'            
            print(self)
            # self.calc_winner()
            if self.is_game_over() == True:
                game_live = False
                break

if __name__ == "__main__":
    Game()
    pass

