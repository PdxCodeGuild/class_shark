"""
Name:           Scott Tran
Date            6/20/2019
Assignment:     Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

    -Less than 17, advise to "Hit"
    -Greater than or equal to 17, but less than 21, advise to "Stay"
    -Exactly 21, advise "Blackjack!"
    -Over 21, advise "Already Busted"

Print out the current total point value and the advice.

"""
import random 


card_values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

x = random.choice(list(card_values.keys()))
y = random.choice(list(card_values.keys()))
z = random.choice(list(card_values.keys()))
   
print(f"Your first card is? {x}.")
print(f"Your second card is? {y}.")
print(f"Your third card is? {z}.")

total = card_values[x] + card_values[x] + card_values[x]

def advice():
    if total < 15:
        print(f"your card total is {total}, you shoud hit again.")
    elif total > 14 and total < 21:
        print(f"your card total is {total}, you shoud stay.")
    elif total == 21:
        print(f"BlackJack!")
    else:
        print(f"Dang {total}, you went over.")


advice()