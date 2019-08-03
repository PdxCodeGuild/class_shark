from random import shuffle, choice
#
# #define card ranks and suits
# card_rank = [i for i in range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace']
# card_suit = ['Spade', 'Heart', 'Diamond', 'Club']
#
# def get_deck():
#     return [[rank, suit] for rank in card_rank for suit in card_suit]
#
# #shuffl deck
# deck = get_deck()
# shuffle(deck)
# #
# def deal_card():
#
# print(deck)


def hand_value():
    deck = {'ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'jack': 10, 'queen': 10, 'king': 10}

    print(deck.keys())

    first_card = input('Pick a card: ').lower()
    first_card_val = deck[first_card]
    second_card = input('Pick a second card: ').lower()
    second_card_val = deck[second_card]
    third_card = input('Pick a third card: ').lower()
    third_card_val = deck[third_card]
    hand_val = first_card_val + second_card_val + third_card_val

    return hand_val

def advice(hand):
    if hand > 21:
        print("Already Busted")
    elif hand == 21:
        print('Blackjack!')
    elif hand >= 17:
        print('Stay')
    elif hand < 17:
        print(" Hit")

    return hand


print(advice(hand_value()))
