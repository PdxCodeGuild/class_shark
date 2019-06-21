# Lab 12: Guess the Number
# Let's play 'Guess the Number'. The computer will guess a random int between 1 and 10. The user will then try to guess the number, and the program will tell them whether they're right or wrong.
# Concepts Covered:
#   - random.randint
#   - REPL: read-evaluate-print loop
#   - input, print
# Version 3:
# Tell the user whether their guess is above ('too high!') or below ('too low!') the target value.

# Import random module
import random


# Define a function, 'Version3' 
def Version3():
    # Display Welcome Screen
    print('Welcome to Version 3 of the Lab 12: Guess the Number. This is a game coded in python by Caleb Mealey.')
    # Display Rules of the game
    print('In this game, the user will be given an unlimited amount of attempts to guess the number that the computer pseudo-randomly picked between 1-10. The computer will keep track of how many guesses the user has made, and tell them at the end.')
    # Display the additional help the computer will provide the user after each guess
    print('In this version, the computer will be share whether each incorrect guess is "too high" or "too low"')
    # Declare a variable, 'x', set its value to be a pseudo-random integer selected between 1-10
    x = random.randint(1,10)
    # Declare a variable, 'guesses', set its value to 0
    guesses = 0
    # Declare a variable, 'TF', set its value to True
    TF = True
    # Initiate the while loop, have it run while 'TF' is True.
    while TF:
        # Declare a variable, 'user_guess', set its value to be the inputted integer the user enters.
        user_guess = int(input('The computer has psuedo-randomly selected an integer between 1 and 10. Enter your guess as to what that number is: '))
        # Check if the inputted 'user_guess' is not equal to 'x', add 1 to the 'guesses' count, display "Try Again!"
        if user_guess != x:
            guesses += 1
            if user_guess > x:
                print('Try Again! Your guess was too high.')
            elif user_guess < x:
                print('Try Again! Your guess was too low.')
        # Check if the inputted 'user_guess' is equal to 'x', add 1 to the 'guesses' count, display "Correct! You guessed ('guesses' count) times"
        elif user_guess == x:
            guesses += 1
            print(f'Your guess, {user_guess}, is correct!')
            # Set 'TF' value to False
            TF = False
    # Display the final print out of how many guesses/tries it took the user to correctly guess the computer's integer
    print(f'It only took you {guesses} tries to correctly guess the computer\'s psuedo-randomly selected integer!')


Version3()
