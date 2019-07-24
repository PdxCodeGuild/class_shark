# Lab 19: Blackjack Advice
# Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:
#   - Less than 17, advise to "Hit"
#   - Greater than or equal to 17, but less than 21, advise to "Stay"
#   - Exactly 21, advise "Blackjack!"
#   - Over 21, advise "Already Busted"
# Print out the current total point value and the advice.

# Version 1: 
# A = 1
# J = 10
# Q = 10
# K = 10
valid_cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
face_cards = ['J', 'Q', 'K']


print('Welcome to Lab 19, also known as Blackjack Advice. This is a program coded in python by Caleb Mealey.')
print('In this game, you will be asked to enter 3 cards. You must enter a valid entry from a traditional 52 playing card deck: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K. After analyzing your inputted 3 cards, the computer will advise whether or not to "Hit", "Stay", if you already have "Blackjack", or if you\'re "Already Busted".')

def playagain():
    answer_list_yes = ['y', 'yes', 'Y', 'Yes', 'YES']
    answer_list_no = ['n', 'no', 'N', 'No', 'NO']
    play_again_tf = True
    while play_again_tf:
        print('Would you like to play again?')
        answer = input('Enter (y)es or (n)o:')
        if answer in answer_list_yes:
            blackjack_advice()
        elif answer in answer_list_no:
            print('Thanks for executing my lab. Come back soon and play again!')
            play_again_tf = False
        else:
            print('Invalid Entry')
            answer = input('Enter (y)es or (n)o:')

def blackjack_advice():
    TF_1 = False
    while not TF_1:
        first_card = input('What\'s your first card? ')
        if first_card in valid_cards:
            if first_card == 'A':
                first_card = 1
            elif first_card in face_cards:
                first_card = 10
            else:
                first_card = int(first_card)
            TF_1 = True
        else:
            print('Invalid Entry. Please enter a valid card.')

    TF_2 = False
    while not TF_2:
        second_card = input('What\'s your second card? ')
        if second_card in valid_cards:
            if second_card == 'A':
                second_card = 1
            elif second_card in face_cards:
                second_card = 10
            else:
                second_card = int(second_card)
            TF_2 = True
        else:
            print('Invalid Entry. Please enter a valid card.')


    TF_3 = False
    while not TF_3:
        third_card = input('What\'s your third card? ')
        if third_card in valid_cards:
            if third_card == 'A':
                third_card = 1
            elif third_card in face_cards:
                third_card = 10
            else:
                third = int(third_card)
            TF_3 = True
        else:
            print('Invalid Entry. Please enter a valid card.')
          
        sum_of_cards = int(first_card) + int(second_card) + int(third_card)
        print(f' Your current total is : {sum_of_cards}')
        if sum_of_cards < 17:
            print('Hit!')
        elif 21 > sum_of_cards >= 17:
            print('Stay')
        elif sum_of_cards == 21:
            print('Blackjack!')
        else:
            print('Already Busted.')

        playagain()

blackjack_advice()



        