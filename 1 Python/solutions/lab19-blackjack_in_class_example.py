def advice(points):
	if points < 17:
		return 'Hit'
	elif 17 <= points < 21:
		return 'Stay'
	elif points == 21:
		return 'Blackjack!'
	else:
		return 'Already Busted'


def calc_points(card):
	card_values = {}
	for i in '23456789':
		card_values[i] = int(i)
	for i in 'JQK':
		card_values[i] = 10
	card_values['A'] = 1
	card_values['10'] = 10

	return card_values[card]


if __name__ == '__main__':
	while True:
		points = 0
		for i in ['first', 'second', 'third']:
			while True:
				card = input(f"What's your {i} card? ").strip().upper()
				if card in 'A23456789JKQ' or card == '10':
					break
			points += calc_points(card)

		print(points, advice(points))

		while True:
			play_again = input("Do you want to play again? ").strip().lower()
			if play_again in ['yes', 'y', 'no', 'n']:
				break

		if play_again in ['no', 'n']:
			break
