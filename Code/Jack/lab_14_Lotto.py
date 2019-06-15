from random import randint


num_of_tickets = 100000


def make_Ticket():
    # ls = []
    # for i in range(6):
    #     ls.append(randint(1, 99))
    #
    # return ls
    return [randint(0, 99) for ls in range(6)]


def winnings(num_matched):
    win = 0
    if num_matched == 6:
        print('YOU WON $25M!!!')
        win = 25000000
    if num_matched == 5:
        print('You won $1M!')
        win = 1000000
    if num_matched == 4:
        win = 50000
    if num_matched == 3:
        win = 100
    if num_matched == 2:
        win = 7
    if num_matched == 1:
        win = 4
    return win


def main():
    money = 0
    winner = make_Ticket()
    num_of_wins = 0
    earnings = 0
    expenses = float(num_of_tickets * 2)
    for i in range(num_of_tickets):
        match = 0
        my_ticket = make_Ticket()
        money -= 2
        i = 0
        for num in winner:
            if num == my_ticket[i]:
                match += 1
                num_of_wins += 1
            i += 1
        earnings += winnings(match)
        money += winnings(match)
    print('\nwinning numbers:', winner
          , '\nMoney: $', money
          , '\nYou won', num_of_wins, 'time(s)'
          , '\nEarnings =', earnings
          , '\nROI:', ((float(earnings)-expenses)/expenses)
          , '\n')



main()
