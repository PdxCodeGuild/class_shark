# Lab 14
# Have the computer play pick6 many times and determine net balance
# Inititally the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.
# A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning number determines the payoff. Order matters, if the winning numbers are [5,10] and your ticket numbers are [10, 5] you have 0 matches. If the winning numberes are [5,10,2] and your ticket numbers are [10,5,2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).
# - a ticket costs $2
# - if 1 number matches, you win $4
# - if 2 numbers match, you win $7
# - if 3 numbers match, you win $100
# - if 4 numbers match, you win $50,000
# - if 5 numbers match, you win $1,000,000
# - if 6 numbers match, you win $25,000,000

import random


def pick_6_winning_ticket():
    winning_numbers = []
    for i in range(6):
        winning_numbers.append(random.choice(range(1, 100)))
    return winning_numbers


def pick_6_purchased_tickets():
    ticket = []
    for z in range(6):
        ticket.append(random.choice(range(1, 100)))
    return ticket


def ticket_matches(winning_ticket, purchased_ticket):
    total_matches = 0
    for y in range(6):
        if winning_ticket[y] == purchased_ticket[y]:
            total_matches += 1
    return total_matches

def ticket_winnings(matches_num):
    winnings = 0
    if matches_num == 1:
        winnings = 4
    elif matches_num == 2:
        winnings = 7
    elif matches_num == 3:
        winnings = 100
    elif matches_num == 4:
        winnings = 50,000
    elif matches_num == 5:
        winnings = 1,000,000
    elif matches_num == 6:
        winnings = 25,000,000
    else:
        winnings = 0
    return winnings


balance = 0
winning_ticket = pick_6_winning_ticket()

for x in range(100001):
    balance -= 2
    balance += ticket_winnings(ticket_matches(winning_ticket, pick_6_purchased_tickets()))

print(balance)