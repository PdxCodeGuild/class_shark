'''
pick6.py

A lottery simulation program
'''

from random import randint

def ticket():
    '''
    returns list of six randomly generated numbers between 1-99
    '''
    return [randint(1, 99) for _ in range(6)]


def payout(ticket, winning_ticket):
    '''
    return payout based on number of matches between a ticket and a winning ticket
    '''
    winnings = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}
    # winnings = [  0,   4,   7,   100,   50000,   1000000,   25000000]

    matches = 0
    for i in range(len(ticket)):
        if ticket[i] == winning_ticket[i]:
            matches += 1 
    return winnings[matches]


def play100k():
    '''
    lottery simulation
    loops 100k times comparing generated tickets to one winning ticket
    '''
    winning_ticket = ticket()
    earnings = 0
    expenses = 0

    for _ in range(100000):
        my_ticket = ticket()
        expenses += 2 
        winnings = payout(my_ticket, winning_ticket)
        earnings += winnings 
        if winnings > 100:
            print(f'RIOT ENGAGES AT ${winnings}')

    print(f'Final balance: ${earnings - expenses}')
    print(f'Return on investment: {(earnings - expenses)/expenses}')    


def loop_until_payout(min_payout=50000):
    '''
    loops until payout equal to :payout: is achieved
    returns number of tickets computed
    '''
    winning_ticket = ticket()
    winnings = 0
    earnings = 0
    expenses = 0
    ticket_count = 0

    while winnings < min_payout:
        expenses += 2
        my_ticket = ticket()
        winnings = payout(my_ticket, winning_ticket)
        earnings += winnings
        ticket_count += 1

        if ticket_count % 500000 == 0:
            print(f'Bought {"{:,}".format(ticket_count)} tickets so far...')

    print(f'Payout of {winnings} after {ticket_count} tickets purchased.')
    print(f'Final balance: ${"{:,}".format(earnings - expenses)}')
    print(f'Return on investment: {(earnings - expenses)/expenses}')    


if __name__ == '__main__':
    # for _ in range(100):
        play100k()
