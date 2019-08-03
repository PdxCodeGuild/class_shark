"""
lab 26: Tic-Tac-Toe
"""

class Player:
	def __init__(self, name, token):
		self.name = name
		self.token = token

	def __repr__(self):
		return self.token

class TicTacToe:
	def __init__(self):
		# self.board = [' ' for x in range(10)]
		self.board = [[' ' for i in range(3)] for j in range(3)]

	def __repr__(self):
		draw_board = ''
		for line in self.board:
			line = [str(token) for token in line]
			draw_board += '|'.join(line) + '\n' 
		return draw_board

		
		# print(self.board[7] + '|' + self.board[8] + '|' + self.board[9])
		# print('-+-+-')
		# print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
		# print('-+-+-')
		# print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])
		
		
	def move(self, x, y, token):
		if type(self.board[y][x]) is Player:  #this checks to see if any Player has taken position
			return False
		
		self.board[y][x] = token
		return True

	def calc_winner(self):
		# check horizontal
		for i in range(3):
			if type(self.board[i][0]) is Player and \
				(self.board[i][0] == self.board[i][1] == self.board[i][2]):
				return self.board[i][0]
		# for i in range(3):
		# 	row = self.board[i]
		# 	if all(item == row[0] and item != ' ' for item in row):
		# 		return row[0]
		
		# check vertical
			if type(self.board[0][i]) is Player and \
				(self.board[0][i] == self.board[1][i] == self.board[2][i]):
				return self.board[0][i]
			# column = [self.board[j][i] for j in range(3)]
			# if all(item == column[0] and item != ' ' for item in column):
			# 	return column[0]
		
		#check diagonal
		if type(self.board[1][1]) is Player:
			if (self.board[0][0] == self.board[1][1] == self.board[2][2]) or \
				(self.board[2][0] == self.board[1][1] == self.board [0][2]):
					return self.board[1][1]
		# if (self.board[0][0] == self.board[1][1] == self.board[2][2] != ' '):
		# 	return self.board[0][0] #doesn't matter which one you return-they are all the same
		# if (self.board[2][0] == self.board[1][1] == self.board [0][2] != ' '):
		# 	return self.board[2][0] # doens't matter which one you return


	def is_full(self):

		for row in self.board:
			for cell in row:
				if cell == " ":
					return False
		return True
		# for row in self.board:
		# 	if any(item ==' ' for item in row):
		# 		return False
		# return True


	def is_game_over(self):

		return self.calc_winner() or self.is_full()



# def draw_board():
# 	print(self.board[7] + '|' + self.board[8] + '|' + self.board[9])
# 	print('-+-+-')
# 	print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
# 	print('-+-+-')
# 	print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])


# def main():

if __name__ == '__main__':

	"""
	coordinate: converts self.board into dic so user can
	retrieve coordinates through keys
	"""
	coordinate = {1: (0,0), 2: (1, 0), 3: (2, 0),
				  4: (0, 1), 5: (1, 1), 6: (2, 1),
				  7: (0, 2), 8: (1, 2), 9: (2,2)}

	while True:
		"""
		Sets up board, player tokens, and player turn tracker
		"""
		player_one = Player('Player One', 'X')
		player_two = Player('Player Two', 'O')
		game_round = 1
		board = TicTacToe()
		
		"""
		Prints a string version of board coordinates
		"""
		help_board = '''The number corresponds to the position on the board:

		1|2|3
		4|5|6
		7|8|9
		'''

		"""
		while is_game_over returns false: players play;
		once it returns, true loop breaks

		player_turn: tracks who turn it is and prints it
		move: ask user for input 1-9 and returns it as an integer

		"""
		while not board.is_game_over():		
			try:
				player_turn = player_one if game_round % 2 else player_two
				move = int(input(f"{player_turn.name}: Enter your move: (1-9) or 0 for help "))		
				"""
				checks if move is between 1-9.
				if true prints new board with tokens placed.
				if move == 0: prints help_board
				"""
				if 1 <= move <= 9:	
					x, y = coordinate[move]					
					move = board.move(x, y, player_turn.token)
					print(board)
					game_round += 1
				elif  move == 0:
					print(help_board)
				else:
					print("Invalid number")
			except ValueError:
				print('Invalid move. Type a number between 1-9.')
		"""
		Finds out if winner or game is a tie
		"""

		if not board.is_full():
			print(f"Game over. {board.calc_winner()} is winner!")
		elif board.calc_winner():
			print(f"Game over. {board.calc_winner()} is winner!")
		else:
			print(f"Game over. Tie.")
			
		"""
		Ask if player would like to play again
		"""

		play_again = input('Play again?: Yes or No?').lower()


		if play_again in ['no', 'n']:
			print('Thanks for playing!')
			break

	


		

		
