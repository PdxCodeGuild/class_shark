from random import choice


def advice(hand):
    cards = [0, 'a', '2', '3', '4',
             '5', '6', '7', '8', '9',
             '10', 'j', 'q', 'k']
    hand_val = []
    ace = 0

    for card in hand:
        if card == 'a':
            ace += 1
        val = cards.index(card)
        if val >= 10:
            val = 10
        hand_val.append(val)
    s_hv = sum(hand_val)
    print('you have', ace, 'ace(s)')
    for _ in range(ace):
        if s_hv < 12:
            s_hv += 10
            print('this ace is worth 11')
    if s_hv > 21:
        return str(s_hv) + ' Already Busted'
    elif s_hv == 21:
        return str(s_hv) + ' Blackjack!'
    elif s_hv >= 17:
        return str(s_hv) + ' Stay'
    else:
        return str(s_hv) + ' Hit'


TF = True
while TF:
    player_hand = [choice(['a', '2', '3', '4', '5',
                           '6', '7', '8', '9', '10',
                           'j', 'q', 'k']) for i in range(3)]
    print(player_hand)
    # player_hand.append(input('first card: ').lower().strip())
    # player_hand.append(input('second card: ').lower().strip())
    # player_hand.append(input('third card: ').lower().strip())
    print(advice(player_hand))
    again = input('another hand? ').lower().strip()
    print('\n')
    if again.startswith('n'):
        TF = False
