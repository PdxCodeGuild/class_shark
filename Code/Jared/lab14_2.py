# lab 14
import random


def pick6():
    random_list = []
    for _ in range(6):
        x = random.randint(1, 99)
        random_list.append(x)
    return random_list
    # return [random.randint(0, 99) for _ in range(6)]

def num_matches(winning, ticket):

    winnings = {0: 0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}
    # winnings = [0, 4, 7, 100, 50000, 100000, 25000000] this is the same as the dictionary because each value can be pulled from the index
    matches = 0
    for i in range(len(winning)):
        if ticket[i] == winning[i]:
            matches += 1
    return winnings[matches]


def play100k():
    earnings = 0
    winning_ticket = pick6()
    expenses = 0
    for _ in range(100000):
        my_ticket = pick6()
        expenses += 2
        winnings = num_matches(my_ticket, winning_ticket)
        earnings += winnings
    print(f'Final balance: {earnings}')
    print(f'Return on investment: {(earnings - expenses)/expenses}')

if __name__ == '__main__':
    for _ in range(100):
        play100k()
# expenses = 0
#
# total_winnings = 0
#
# for i in range(100000):
#     expenses -= 2
#     total_winnings += winnings(num_matches('', ''))
#
# earnings = total_winnings - expenses
#print(winning_ticket, my_ticket, winnings, balance)
# print(earnings)
#
#
# print(pick6())
# print(winnings)
# print(num_matches('', ''))
# print(winnings(num_matches('', '')))
# print(total_winnings)
