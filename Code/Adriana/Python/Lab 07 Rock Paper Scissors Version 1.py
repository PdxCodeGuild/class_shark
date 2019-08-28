#LAB 07 Rock, Paper, Scissors
#Step 1 The computer will ask the user for their choice (rock, paper, scissors)
#Step 2 The computer will randomly choose rock, paper or scissors
#Step 3 Determine who won and tell the user

import random
decide = ['rock', 'paper', 'scissors']

user_selection = input(f"rock, paper, or scissors?" )
opponent_selection = (random.choice(decide))
print(opponent_selection)

if user_selection == opponent_selection:
    print('tie')

if user_selection == 'rock':
    if opponent_selection == 'paper':
        print ('You Lose. Try Again')
    elif opponent_selection == 'scissors':
        print ('You Won.')

if user_selection == 'paper':
    if opponent_selection == 'scissors':
        print ('You Lose. Try Again')
    elif opponent_selection == 'rock':
        print ('You Won.')

if user_selection == 'scissors':
    if opponent_selection == 'rock':
        print ('You Lose. Try Again')
    elif opponent_selection == 'paper':
        print ('You Won.')
