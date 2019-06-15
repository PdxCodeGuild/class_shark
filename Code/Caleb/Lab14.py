# Lab 14: Pick 6
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

# Import Random Module
import random

# Display Welcome Screen
print('Welcome to Lab 14, a program coded in python by Caleb Mealey')

# Define a function 'pick_6', will shoot out a random ticket of 6 numbers between 1-99
def pick_6():
    ticket = []
    for i in range(6):
        ticket.append(random.choice(range(1, 99)))
    return ticket

# Define a function 'ticket_matches' that counts how many matches a ticket has when analyzed against the winning ticket
def ticket_matches(winning_ticket, purchased_ticket):
    total_matches = 0
    for y in range(6):
        if winning_ticket[y] == purchased_ticket[y]:
            total_matches += 1
    return total_matches

# Define a function 'ticket_winnings' that will return the total winnings an individual ticket earned
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
    return winnings

expenses = 0
earnings = 0
final_balance = 0
winning_ticket = pick_6()

for x in range(100000):
    expenses -= 2
    earnings += ticket_winnings(ticket_matches(winning_ticket, pick_6()))

final_balance = earnings + expenses
ROI = (earnings - expenses) / expenses

print('-' * 60)
print(f'The winning ticket was: {winning_ticket}')
print('-' * 60)
print(f'After purchasing 100,000 tickets, your total earnings was: ${earnings}')
print(f'After purchasing 100,000 tickets, your total expenses was: ${expenses}')
print('-' * 60)
print(f'After purchasing 100,000 tickets, your ROI (return on investment) was: ${ROI}')
print('-' * 60)
