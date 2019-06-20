import random
import math


def computer_Num_Vs_User():

    num_Of_Guesses = 0
    user_Prev_Guess = 0
    comp_Num = random.randint(0, 1000)
    t_Cont = True
    print('I have picked a number between 0 and 1000\n')

    '''First round so it doesn't give the closer or farther txt'''
    user_Guess = int(input(f'please enter your guess: \n'))
    if (user_Guess > 1000) or (user_Guess < 0):
        print('Your Guess was out of bounds try again\n')
        t_Cont = False
    elif user_Guess == comp_Num:
        print(f'My number WAS {user_Guess} YOU WIN!\n')
        t_Cont = False
    else:
        if user_Guess < comp_Num:
            print('\nMy number is higher')
        else:
            print('\nMy number is lower')
        user_Prev_Guess = user_Guess
        num_Of_Guesses += 1
        print(f'You have {10 - num_Of_Guesses} guesses left\n')


    while t_Cont:
        user_Guess = int(input(f'please enter your guess: \n'))
        if (user_Guess > 1000) or (user_Guess < 0):
            print('Your Guess was out of bounds try again\n')
            t_Cont = False
        elif user_Guess == comp_Num:
            print(f'My number WAS {user_Guess} YOU WIN!\n')
            t_Cont = False
        else:
            guess_Dist(user_Guess, user_Prev_Guess, comp_Num)
            if user_Guess < comp_Num:
                print('My number is higher')
            else:
                print('My number is lower')
            user_Prev_Guess = user_Guess
            num_Of_Guesses += 1
            print(f'You have {10 - num_Of_Guesses} guesses left\n')
        if num_Of_Guesses >= 10:
            print(f'Thats 10 guesses, my number was {comp_Num} '
                    + 'I WIN!\n')
            t_Cont = False


def user_Num_Vs_Computer():
    print('Pick a number between 0 and 1000\n')
    t_Cont = True
    guess = random.randint(0, 1000)
    t_Guess = guess - 1
    prev_Guess = guess + 1

    hL = input(f'Is it higher or lower than {guess}?\n'
                + 'Higher:      1\n'
                + 'Lower:       2\n'
                + 'Thats IT!    3\n')
    if check(hL):
        if hL == '1':
            t_Guess = guess
            guess = math.floor(guess + (1000 - guess))
            prev_Guess = t_Guess
        elif hL == '2':
            t_Guess = guess
            guess = guess - (guess/2)
            prev_Guess = t_Guess
    else:
        print('incorrect input')
        t_Cont = False

    while t_Cont:
        if guess == prev_Guess:
            prev_Guess += 10
            print('Im Here')
        hL = input(f'Is it higher or lower than {int(guess)}?\n'
                    + 'Higher:      1\n'
                    + 'Lower:       2\n'
                    + 'THATS IT!    3\n')
        if hL == '1':
            t_Guess = guess
            guess = math.floor(guess + abs((prev_Guess - guess)/2))
            prev_Guess = t_Guess
        elif hL == '2':
            t_Guess = guess
            guess = math.floor(guess - (abs((guess - prev_Guess)/2)))
            prev_Guess = t_Guess
        elif hL == '3':
            print('I WIN!')
            t_Cont = False
        else:
            print('incorrect input')
            t_Cont = False


def guess_Dist(user_Guess, user_Prev_Guess, comp_Num):
    cur_Dist = abs(user_Guess - comp_Num)
    prev_Dist = abs(user_Prev_Guess - comp_Num)

    if cur_Dist <= prev_Dist:
        print('\nyour closer than last time')
    else:
        print('\nyour last guess was closer')


def check(hL):
    if hL == '1' or hL == '2':
        return True
    elif hL == '3':
        print('I WIN!!!!')
        return False
    else:
        print('\nincorrect input:\n')
        return False


def menu_One():
    menu_Choice = int(input('Welcome to the Guessing Game!\n'
                    + 'Please make a selection from the following:\n'
                    + 'You guess my number:     1\n'
                    + 'I guess YOUR number:     2\n'))
    return menu_Choice


def again():
    choice = input('would you like to go again? y/n\n')
    if choice == 'y':
        return True
    elif choice == 'n':
        print('\nGoodBye!\n')
        return False
    else:
        print('\nincorrect input:\n')
        return True


TF = True
while TF:
    choice = menu_One()
    if choice == 1:
        computer_Num_Vs_User()
    elif choice == 2:
        user_Num_Vs_Computer()
    else:
        print('\ninvalid input\n')
    TF = again()
