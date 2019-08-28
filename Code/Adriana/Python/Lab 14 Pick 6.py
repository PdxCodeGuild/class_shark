#LAB 14: PICK 6 - LOTO

#COMPUTER PICKS 6 NUMBERS RANDOM & DETERMINE NET BALANCE

#TICKET NUMBER WILL BE ANYWHERE FROM 1 TO 99

#MATCHES DETERMINS THE PAYOUT

#CALCULATE YOUR NET WINNINGS

#a ticket costs $2
#if 1 number matches, you win $4
#if 2 numbers match, you win $7
#if 3 numbers match, you win $100
#if 4 numbers match, you win $50,000
#if 5 numbers match, you win $1,000,000
#if 6 numbers match, you win $25,000,000

import random

#first select 6 random numbers
#function will be called in main function
def pick6():
    #selects six random numbers between 1-99
    ticket = []
    for _ in range(6):
        ticket.append(random.randint(1,99))
    return ticket

#class notes:
#def ticket():
    #return [randint(1,99) for _ in range(6)]

def winning_payout(winning, ticket):
    #this function will compare the winning ticket and your ticket and see how many numbers match
    #class notes: can set up a list or dictionary

    winnings= [0,4,7,100,50000,100000,2500000]
    matches = 0
    for i in range(len(ticket)):
        if winning[i] == ticket[i]:
            matches += 1
            #if the ticket numbers match the winning ticket then 1 will be added to the total number of matches
    return winnings[matches]

def play100k():
    #this function will loop 100k times comparing to one potentially winning ticket
    #this is basically the lottery simulation
    #follow steps in lab

    winning = pick6()
    #when winning equals the 6 random
    balance = 0
    #this is to keep track of running balance
    #expenses = 0 => this is to keep track of expenses

    for i in range(100000):
        ticket = pick6()
        balance -= 2
        payout = winning_payout(winning,ticket)
        balance += payout

    print(f'Balance:', balance)

    if __name__ == '__main__':
        #for _ in range(100) - how we wrote it in class
        play100k()

