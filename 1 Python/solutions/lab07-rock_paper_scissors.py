"""
Lab 7: play rock-paper-scissors with the computer
"""

import random

rps = ['rock', 'paper', 'scissors'] #list of possible options

while True:
	while True:
	    user_choice = input('rock, paper, or scissors? ').lower().strip()
	    if user_choice in rps:
	        break

	print('user choice: ' + user_choice)

	comp_choice = random.choice(rps)
	print('computer choice: ' + comp_choice)

	# rock - paper
	# rock - scissors
	# paper - rock
	# paper - scissors
	# scissors - rock
	# scissors - paper

	if user_choice == comp_choice:
	    print('tie!')
	elif user_choice == 'rock' and comp_choice == 'paper':
	    print('computer wins!')
	elif user_choice == 'rock' and comp_choice == 'scissors':
	    print('user wins!')
	elif user_choice == 'paper' and comp_choice == 'rock':
	    print('user wins!')
	elif user_choice == 'paper' and comp_choice == 'scissors':
	    print('computer wins!')
	elif user_choice == 'scissors' and comp_choice == 'rock':
	    print('computer wins!')
	elif user_choice == 'scissors' and comp_choice == 'paper':
	    print('user wins!')

	# Checks for valid input
	while True:
		play_again = input("Do you want to play again? ").lower().strip()
		if play_again == 'yes' or play_again == 'no':
			break

	# Exits outer while loop and ends program if user chooses no
	if play_again == 'no':
		break