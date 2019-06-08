# lab 7 - rps.py

from random import choice 

# def calc_winner(user, computer):
#     '''
#     returns which player won
#     '''
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
#     elif user == 'scissors' and computer == 'rock':
#         return 'Computer'
#     elif user == 'scissors' and computer == 'paper':
#         return 'User'


def calc_winner(user, computer):
    '''
    dictionary implementation
    returns which player won
    '''
    loses_to = {'rock':'scissors', 'paper':'rock', 'scissors': 'paper'}

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
    valid_choices = ('rock', 'paper', 'scissors')

    # input validation
    invalid = True
    while invalid:
        user_choice = input('rock, paper, scissors: ').lower().strip()
        if user_choice in valid_choices:
            invalid = False

    computer_choice = choice(valid_choices)

    print('-'*60)
    print('User: ' +user_choice)
    print('Computer: ' +computer_choice)
    print('-'*60)

    winner = calc_winner(user_choice, computer_choice)

    print('Winner: ' +winner)
    print('-'*60)

    # input validation
    invalid = True 
    while invalid:
        play_ag = input('Do you want to play again: ').strip().lower()
        if play_ag in ['yes', 'no', 'y', 'n']:
            invalid = False
    print('-'*60)

    # returns tuple of play again and winner
    return play_ag.startswith('y'), winner


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
        play_again, winner = play()
        wins[winner] += 1  # increment winner         
        rounds += 1        # increment round 

    print('Total wins')
    print('-'*60)
    for winner in wins:
        print(f'{winner}: {wins[winner]}')
    print('-'*60)
    print('Goodbye!')