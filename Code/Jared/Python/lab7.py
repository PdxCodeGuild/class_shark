# Paper-Scissors-Rock
import random
computer_hand = ('rock', 'paper', 'scissors')
computer_weapon = random.choice(computer_hand)

user_hand = input("Rock, paper, scissors: (choose)")

print('The computer choose:' + computer_weapon)

if computer_weapon == user_hand:
    print('It\'s a tie!')
elif computer_weapon != user_hand:
    if computer_weapon == 'rock' and user_hand != 'paper':
        print('Computer wins. You lose.')
    elif computer_weapon == 'paper' and user_hand != 'scissors':
        print('Computer wins. You lose.')
    elif computer_weapon == 'scissors' and user_hand != 'rock':
        print('Computer wins. You lose.')
    else:
        print('You win!')
