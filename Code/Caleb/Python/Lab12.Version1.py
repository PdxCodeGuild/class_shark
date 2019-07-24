# Lab 12: Guess the Number
# Let's play 'Guess the Number'. The computer will guess a random int between 1 and 10. The user will then try to guess the number, and the program will tell them whether they're right or wrong.
# Concepts Covered:
#   - random.randint
#   - REPL: read-evaluate-print loop
#   - input, print
# Version 1:
# Using a while loop, allow the user to guess 10 times. If they fail to guess the number after 10 tries, the user is told they've lsot. If the user guesses the nubmer, the user is told they've won and the game exits. You can get a random number using random.randint:
#   import random
#   x = random.randint(1,10)
#   print(x)
# Below is an example run of the game:
#   guess the number: 5
#   try again!
#   guess the number: 2
#   try again!
#   guess the number: 3
#   correct! you guessed 3 times

# Import random module
import random

# Define a function, 'Version1' 
def Version1():
    # Display Welcome Screen
    print('Welcome to Version 1 of the Lab 12: Guess the Number. This is a game coded in python by Caleb Mealey.')
    # Display Rules of the game
    print('In this game, the user will be given 10 attempts to guess the number that the computer pseudo-randomly picked between 1-10. After each guess the computer will respond whether or not the guess was correct.')
    # Declare a variable, 'x', set its value to be a pseudo-random integer selected between 1-10
    x = random.randint(1,10)
    # Declare a variable, 'guesses', set its value to 0
    guesses = 0
    # Initiate the while loop, have it run while 'guesses' value is less than 10
    while guesses < 10:
        # Declare a variable, 'user_guess', set its value to be the inputted integer the user enters.
        user_guess = int(input('The computer has psuedo-randomly selected an integer between 1 and 10. Enter your guess as to what that number is: '))
        # Check if the inputted 'user_guess' is not equal to 'x', add 1 to the 'guesses' count, display "Try Again!"
        if user_guess != x:
            guesses += 1
            print('Try Again!')
        # Check if the inputted 'user_guess' is equal to 'x', add 1 to the 'guesses' count, display "Correct! You guessed ('guesses' count) times"
        elif user_guess == x:
            guesses += 1
            print(f'Correct! You guessed {guesses} times')
            # Break out of the loop to end the game
            break
    # Display "Game Over", as the user attempted 10 times and failed            
    print('Game Over!')


Version1()
