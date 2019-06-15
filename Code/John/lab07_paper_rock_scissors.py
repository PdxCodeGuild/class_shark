# paper_rock_scissors_v2.py

import random
cont ='y'
print('\n' + 'Welcome to Paper Rock Scissors, I hope you\'re ready!' + '\n' )
while cont == 'y':
    choice_list = ['rock','paper','scissors']
    npc_choice = random.choice(choice_list)
    user_choice = input(f'What is your choice for ro sham bo? {choice_list[0]}, {choice_list[1]}, or {choice_list[2]}: ')
    while user_choice not in choice_list:
        print('\n')
        user_choice = input(f'I\'m sorry, that is not a valid choice. Remember capitalization matters! Please select from the following: {choice_list[0]}, {choice_list[1]}, or {choice_list[2]}: ')
    print(f"\nYour opponent chose: {npc_choice.capitalize()} \n")
    if npc_choice == user_choice:
        print("It's a tie!\n")
    elif npc_choice == choice_list[0]:
        if user_choice == choice_list[1]:
            print("Congrats!! You're the WINNER!!!\n")
        else:
            print("Sorry, better luck next time!\n")
    elif npc_choice == choice_list[1]:
        if user_choice == choice_list[0]:
            print("Sorry, better luck next time!\n")
        else:
            print("Congrats!! You're the WINNER!!!\n")
    elif npc_choice == choice_list[2]:
        if user_choice == choice_list[0]:
            print("Congrats!! You're the WINNER!!!\n")
        else:
            print("Sorry, better luck next time!\n")
    cont = input("Do you want to play again? (y/n): ")
