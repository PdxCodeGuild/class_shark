from random import randint


num_of_tickets = 100000


def make_Ticket():
    # ls = []
    # for i in range(6):
    #     ls.append(randint(1, 99))
    #
    # return ls
    return [randint(1, 99) for _ in range(6)]


def find_matches(win_ticket, my_ticket):
    winnings = [0, 4, 7, 100, 50000, 1000000, 25000000]
    match = 0
    for i in range(6):
        if my_ticket[i] == win_ticket[i]:
            match += 1
    return winnings[match]


def main():
    money = 0
    num_of_wins = 0
    earnings = 0
    expenses = float(num_of_tickets * 2)

    winner = make_Ticket()

    for itm in range(num_of_tickets):
        money -= 2
        my_ticket = make_Ticket()
        t_money = find_matches(winner, my_ticket)
        if t_money > 0:
            money += t_money
            earnings += t_money
            num_of_wins += 1

    print('\nwinning numbers:', winner
          , '\nMoney: $', money
          , '\nYou won', num_of_wins, 'time(s)'
          , '\nEarnings =', earnings
          , '\nROI:', ((float(earnings)-expenses)/expenses)
          , '\n')



main()
