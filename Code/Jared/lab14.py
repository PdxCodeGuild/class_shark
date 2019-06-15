# lab 14
import random


def pick6():
    random_list = []
    for i in range(6):
        x = random.randint(1, 100)
        random_list.append(x)
    return random_list


def num_matches(winning, ticket):
    # winning = [1, 3, 5, 5, 6, 7]
    #ticket = [1 , 3, 5, 6, 3, 2]
    winning = pick6()
    ticket = pick6()
    matches = 0
    for num in range(len(winning)):
        if ticket[num] == winning[num]:
            matches += 1
    return matches


def winnings(matches):
    money_won = 0
    if matches == 1:
        money_won = 4
    elif matches == 2:
        money_won = 7
    elif matches == 3:
        money_won = 100
    elif matches == 4:
        money_won = 50000
    elif matches == 5:
        money_won = 1000000
    elif matches == 6:
        money_won = 25000000
    return money_won


expenses = 0

for i in range(100000):
    expenses -= 2
    winnings += ticket_winnings(num_matches('', ''))

earnings = expenses + winnings

print(earnings)


# print(pick6())
# print(my_nums())
# print(ticket_winnings(num_matches('', '')))
