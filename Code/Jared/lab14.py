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
total_winnings = 0
for i in range(100000):
    expenses -= 2
    total_winnings += winnings(num_matches('', ''))

earnings = total_winnings - expenses

print(earnings)


print(pick6())
print(num_matches('', ''))
print(winnings(num_matches('', '')))
print(total_winnings)
