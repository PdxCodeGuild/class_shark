"""
Name:           Scott Tran
Date            6/7/2019
Assignment:     The computer will guess a random int between 1 and 10. The user will then try to guess the number, and the program will tell them whether they're right or wrong. Allow the user to make an unlimited number of guesses using a while True and break. Keep track of how many guesses the user has made, and tell them at the end.
"""

import random

x = random.randint(1,10)
count = 0


def guess():
    while True:
        try:
            i = int(input("Guess the number between 1-10: "))
            if i in range(1, 11):
                return i
            else:
                print(f"{i} was not an number bewtween 1-10. Please try again...") 
        except ValueError:
            print("No valid integer! Please try again ...")


while True:
    g = guess()
    if g == x:
        print(f"Correct! you guessed {count} times.")
        break
    else:
        count += 1
        print("Incorrect, try again.")
