# LAB 19 BLACKJACK ADVICE
# First ask user for three playing cards
# Figure out point value
# Advice is based on the below:
# Less than 17, advise to "Hit"
# Greater than or equal to 17, but less than 21, advise to "Stay"
# Exactly 21, advise "Blackjack!"
# Over 21, advise "Already Busted"


def card_value(input_card):
    if input_card in ("A", "K", "Q", "J", "Ace", "King", "Queen", "Jack"):
        input_card = 10
    else:
        input_card = int(input_card)
    return input_card


def main():
    first_card = input(f'Whats your first card? ')
    second_card = input(f'Whats your second card?  ')
    third_card = input(f'Whats your third card?  ')

    print(first_card, second_card, third_card)

    card_total = card_value(first_card) + card_value(second_card) + card_value(third_card)

    print(card_total)

    if card_total < 17:
        print("Hit")
    elif card_total < 21:
        print("Stay")
    elif card_total == 21:
        print("BlackJack!")
    else:
        print("Busted!")
