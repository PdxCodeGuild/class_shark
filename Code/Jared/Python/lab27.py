# Connect Four
class Player:
	def __init__(self, name, color):
		self.name = name
		self.color = color

	def __repr__(self):
		return self.color

class Game:
	"""
	get_height(position): returns int of how many pieces occupy a column
	move(player, position): adds a player token to a column after figuring out the current height of the column
	calc_winner(): returns true if a match (four in a row) is found
	is_full(): returns true if all board positions are occupied
	is_game_over(): returns true if the game is over (a winner is found or the board is full
	"""
	DEPTH = 6
	WIDTH = 7

	def __init__(self):
		self.board = [[' ' for _ in range(self.WIDTH)] for _ in range(self.DEPTH)]

	def __repr__(self):
		draw_board = ''
		for column in self.board:
			column = [str(color) for color in column]
			draw_board += '|'.join(column) + '\n'
		return draw_board

	def get_height(self, position, player):
		for i in range(self.DEPTH-1, -1, -1):
			if self.board[i][position] == ' ':
				return i 
		return False # Column Full

	def move(self, color, position):
		m = board.get_height(position)
		if type(m) is bool:
			print('Column is full')
			return False
		self.board[m][position] = color


	def calc_winner(self):
		for i in range(self.DEPTH-1, -1, -1):
			for j in range(self.WIDTH):
		
				# horizontal
				if j < self.WIDTH-3:
					chunk = self.board[i][j:j+4]
					if all(item == self.board[i][j] and item != ' ' for item in chunk):
						print('OHBOY')
						print(chunk)
						return True

				# vertical
				if i < self.DEPTH-3:
					chunk = []
					chunk.append(self.board[i][j])
					chunk.append(self.board[i+1][j])
					chunk.append(self.board[i+2][j])
					chunk.append(self.board[i+3][j])
					if all(item == self.board[i][j] and item != ' ' for item in chunk):
						print('YAY!')
						return True

				# diagonal
 			# if i < self.DEPTH-3 and j < self.WIDTH-3:
				# 	chunk.append()

				# right diagonal
			for i in range(board.WIDTH-3):
				for j in range(3, board.DEPTH):
					if self.board[i][j] == self.board

				#left diagonal


		
	def is_full(self):
		for x in self.board:
			if any(item==' ' for item in x):
				return False
		return True

	def is_game_over(self):
		return self.calc_winner() and self.is_full()

if __name__ == '__main__':

	player_one = Player('Player One', 'R')
	player_two = Player('Player Two', 'B')
	board = Game()
	print(board)
	print(board.move(player_one, 4))
	print(board)
	# print(board.move(player_two, 3))
	print(board)
	print(board.move(player_one, 4))
	print(board)
	print(board.move(player_one, 4))
	print(board)
	print(board.get_height(4))
	print(board.get_height(3))
	print(board.move(player_one, 4))
	print(board)
	print(board.calc_winner())
	print(board.move(player_two, 2))
	print(board.move(player_two, 1))
	print(board.move(player_two, 0))
	print(board)
	print(board.calc_winner())


	