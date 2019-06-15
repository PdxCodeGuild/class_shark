# Lab 7 : Rock, Paper, Scissors
#   Let's play rock-paper-scissors with the computer.

#   The computer will ask the user for their choice (rock, paper, scissors)
#   The computer will randomly choose rock, paper or scissors
#   Determine who won and tell the user
# Let's list all the cases:
#   rock vs rock (tie)
#   rock vs paper
#   rock vs scissors
#   paper vs rock
#   paper vs paper
#   paper vs scissors
#   scissors vs rock
#   scissors vs paper
#   scissors vs scissors

# Version 2 (optional)
#   After playing, ask them if they'd like to play again. If they say yes, restart the game, otherwise exit.

# import random module
from random import choice

# Display Welcome Screen
print("Welcome to the Rock, Paper, & Scissors Game developed after the classic original by Caleb Mealey in Python")

# game_moves = {'rock': 'rock', 'rock': 'paper', 'rock': 'scissors', 'paper': 'rock', 'paper': 'paper', 'paper', 'scissors', 'scissors': 'rock', 'scissors': 'paper', 'scissors':'scissors'}

# def calc_winner(user, computer):
#     ##     returns which player won
#     if user == computer:
#         return 'Tie'
#     elif user == 'rock' and computer == 'paper':
#         return 'Computer'
#     elif user == 'rock' and computer == 'scissors':
#         return 'User'
#     elif user == 'paper' and computer == 'rock':
#         return 'User'
#     elif user == 'paper' and computer == 'scissors':
#         return 'Computer'
#     elif user == 'scissors' and computer == 'paper':
#         return 'User'
#     elif user == 'scissors' and computer == 'rock':
#         return 'Computer'

def calc_winner(user, computer):
    '''
    dictionary implementation
    returns which player won
    '''
    loses_to = {'rock': 'scissors', 'paper': 'rock', 'scissors':'paper'}

    if user == computer:
        return 'Tie'
    elif loses_to[user] == computer:
        return 'User'
    else:
        return 'Computer'

def play():
    '''
    rock paper scissors game logic
    '''
    valid_choices = ['rock', 'paper', 'scissors']
    
# Input Validation
    invalid = True
    while invalid:
        user_choice = input('rock, paper, scissors: ').lower().strip()
        if user_choice in valid_choices:
            invalid = False
        else:
            print('Invalid! Please enter "rock, paper, or scissors": ')
    computer_choice = choice(valid_choices)
    print('-'*60)
    print('User: ' + user_choice)
    print('Computer: ' + computer_choice)
    print('-'*60)
    winner = calc_winner(user_choice, computer_choice)
    print('Winner: ' + winner)
    print('-'*60)

    invalid = True
    while invalid:
        play_again_answer = (input("Would you like to play again? Enter 'yes' or 'y' to continue playing, or 'no' or 'n' to end your session: ").lower().strip()
        if play_again_answer in ['yes', 'no', 'y', 'n']
            invalid = False
    print('-'*60)
    return play_again_answer.startswith('y'), winner

    play_again = True
    wins = {
        'User': 0,
        'Computer': 0,
        'Tie': 0
    }
    rounds = 1

# loop gameplay
    print('-'*60)
    while play_again:
        play_again = play()
        wins[winner] += 1   # increment winner
        rounds += 1         # increment round
    print('Total wins')
    print('-'*60)
    for winner in wins:
        print(f'{winner}: {wins[winner]}')
    print('-'*60)
    print('Goodbye!')

if __name__ == '__main__':
    # # tests
    # print(calc_winner('scissors', 'rock'))
    # print(calc_winner('rock', 'scissors'))
    # print(calc_winner('scissors', 'paper'))
    # print(calc_winner('paper', 'rock'))
    # print(calc_winner('rock', 'paper'))
    # print(calc_winner('scissors', 'scissors'))
    # print(calc_winner('paper', 'paper'))
    # print(calc_winner('rock', 'rock'))

    # print('in main', __name__)

play()