from random import choice

#directions = [[(y, x) for y in range(-1, 2) if (y, x) != (0, 0)] for x in range(-1, 2)]
directions = []
for x in range(-1, 2):
	for y in range(-1, 2):
		if (y, x) != (0, 0):
			directions.append((y, x))
direction_dict = {
	(-1, 0): 'North',
	(-1, 1): 'Northeast',
	(0, 1): 'East',
	(1, 1): 'Southeast',
	(1, 0): 'South',
	(1, -1): 'Southwest',
	(0, -1): 'West',
	(-1, -1): 'Northwest',
}
class Board:
	def __init__(self, width, height, win_length):
		self.width = width
		self.height = height
		self.win_length = win_length
		self.board = [[choice('XO') for x in range(self.width)] for y in range(self.height)]
		self.solutions = []

	def __repr__(self):
		return f"Board({self.width}, {self.height}, {self.win_length})"

	def print_board(self):
		print('\n'.join(['|'.join(row) for row in self.board]))

	def check_for_matches(self):
		self.solutions = []
		for x in range(self.width):
			for y in range(self.height):
				for direction in directions:
					self.crawl((y, x), direction, self.board[y][x])
	
	def crawl(self, position, direction, player):
		next_pos = (position[0] + direction[0], position[1] + direction[1])
		if 0 <= next_pos[0] < self.height and 0 <= next_pos[1] < self.width and \
		self.board[next_pos[0]][next_pos[1]] == player:
			self.crawl(next_pos, direction, player)
		else:
			self.match(position, (direction[0] * -1, direction[1] * -1), player, 1)

	def match(self, position, direction, player, matches):
		next_pos = (position[0] + direction[0], position[1] + direction[1])
		if 0 <= next_pos[0] < self.height and 0 <= next_pos[1] < self.width and \
		self.board[next_pos[0]][next_pos[1]] == player:
			self.match(next_pos, direction, player, matches + 1)
		elif matches >= self.win_length:
			self.solutions.append(f"DOWN: {position[0]}, RIGHT: {position[1]} got {matches} {player}s travelling in direction {direction_dict[direction]}.")

	
my_board = Board(10, 10, 7)
my_board.print_board()
my_board.check_for_matches()
print(set(my_board.solutions))
