# lab12_guess_the_number.py

import random
num1 = random.randint(1, 10)
tries = 0
while tries < 10:
    guess = int(input('\n' + 'Guess a number between 1 and 10, you have 10 tries! > '))
#    guess = int(guess)
    if guess == num1:
        print('\n' + 'You guessed it!')
        break
    else:
        print('\n' + f'Sorry, incorrect!')
        tries += 1
print('\n' + f'You used a total of  {tries} tries')
