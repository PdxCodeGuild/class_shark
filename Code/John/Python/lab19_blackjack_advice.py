# lab19_blackjack_advice.py

advisor = {range(0, 17): 'hit!!', range(17, 21): 'stay!!',
           (21,): 'BLACKJACK!!', range(22, 100): 'Already busted, sorry!'}
cards = {'a': 1, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
         '8': 8, '9': 9, '10': 10, 'j': 10, 'q': 10, 'k': 10}
total = 0
hand_count = 0

print(f"\n\t\tWelcome to Blackjack!! Remember, the nomenclature for the cards\
 here:\n\t\t\tA, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K")

while hand_count < 3:
    if hand_count == 0:
        card1 = input("\nWhat is your first card? ")
        if card1 in cards:
            total += cards.get(card1)
            hand_count += 1
        else:
            print("\nSorry, I don't recognize that card")

    elif hand_count == 1:
        card2 = input("What is your second card? ")
        if card2 in cards:
            total += cards.get(card2)
            hand_count += 1
        else:
            print("\nSorry, I don't recognize that card")

    elif hand_count == 2:
        card3 = input("What is your third card? ")
        if card3 in cards:
            total += cards.get(card3)
            hand_count += 1
        else:
            print("\nSorry, I don't recognize that card")

if total <= 11:
    if card1 == 'a' or card2 == 'a' or card3 == 'a':
        total += 10

for num_range in advisor:
    if total in num_range:
        advice = advisor[num_range]
        print(f"{total} {advice}")
