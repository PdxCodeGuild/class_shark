"""
Name:           Scott Tran
Date            6/6/2019
Assignment:     Pay rock-paper-scissors with the computer
"""

import random



pick = ['rock', 'paper', 'scissors']

Play = True

while Play:

    user_pick = input("Lets play paper-rock-scissors! Choose one: ")

    computer_pick = random.choice(pick)

    print(f"The computer selects {computer_pick}.")

    if user_pick == computer_pick:
        print("Tie.")
    elif user_pick == 'rock' and computer_pick == 'scissors':
        print("You win!")
    elif user_pick == 'rock' and computer_pick == 'paper':
        print("You lose!")
    elif user_pick == 'scissors' and computer_pick == 'rock':
        print("You lose!")
    elif user_pick == 'scissors' and computer_pick == 'paper':
        print("You win!")
    elif user_pick == 'paper' and computer_pick == 'scissors':
        print("You lose!")
    elif user_pick == 'paper' and computer_pick == 'rock':
        print("You win!")
    else:
        print(f"That wasn't one of the choices....")

    again = input("\nWould you like to ask again? please type 'yes' or 'no':  ")
    if again == "no":
        Play = False