"""
Name:           Scott Tran
Date            6/11/2019
Assignment:     Have the computer play pick6 many times and determine net balance.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).

The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses.
"""

import random

wins = 0


def pick6():
    ticket = []
    for i in range(6):
        # print('i')
        x = random.randint(1, 99)
        ticket.append(x)
    return ticket


def match():
    my_ticket = pick6()
    lottery = pick6()
    matches = 0
    for i in range(6):
        if my_ticket[i] == lottery[i]:
            matches += 1
    return matches

    if matches == 0:
        return 0
    elif matches == 1:
        return 4
    elif matches == 2:
        return 7
    elif matches == 3:
        return 100
    elif matches == 4:
        return 50000
    elif matches == 5:
        return 1000000
    elif matches == 6:
        return 25000000
    else:
        print('error')
        

def cycle(x):
    count = 0
    for i in range(x):
        count += match()
    return count


play = int(input("How many lottery tickets would you like to buy?" ))
pretty_play = "{:,}".format(play)


games = cycle(play)
pretty_games = "{:,}".format(games)


cost = int(play*2)
pretty_cost = "{:,}".format(cost)

net_investment = "{:,}".format(games - cost)
roi = round((games-cost)/cost*100,0)


print(f"\nIf you play the lottery {pretty_play} times, it will cost you {pretty_cost} dollars and you will make {pretty_games} dollars in return. Your net investment will be {net_investment} with an ROI of {roi}%.")