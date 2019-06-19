import random
import string

def password_Generator(char_Lower_Count, char_Upper_Count,
                        digit_Count, punc_Count):

    t_Pass = []
    for i in range(0,char_Lower_Count):
        t_Pass.append(random.choice(list(string.ascii_lowercase)))
    for i in range(0,char_Upper_Count):
        t_Pass.append(random.choice(list(string.ascii_uppercase)))
    for i in range(0,digit_Count):
        t_Pass.append(str(random.randint(0,9)))
    for i in range(0,punc_Count):
        t_Pass.append(random.choice(list(string.punctuation)))
    t_Pass = list(t_Pass)
    random.shuffle(t_Pass)
    s = ''
    return s.join(t_Pass)

def menu_One():
    menu_Choice = input('Welcome to the password generator!\n'
                    + 'Please make a selection from the following:\n'
                    + 'Random 10 digit password:        1\n'
                    + 'User defined random password:    2\n')
    return menu_Choice

def menu_Two():
    num_Of_Characters = int(input('How many digits do you want '
                              + 'in your password? '))
    num_Of_Lowercase = int(input('\nHow many lowercase letters would '
                              + 'you like in your password?\n'))
    num_Of_Characters -= num_Of_Lowercase
    desired_Num_Of_Char(num_Of_Characters)
    num_Of_Uppercase = int(input('\nHow many uppercase letters would '
                              + 'you like in your password?\n'))
    num_Of_Characters -= num_Of_Uppercase
    desired_Num_Of_Char(num_Of_Characters)
    num_Of_Num = int(input('\nHow many numbers would you like in your '
                              + 'password?\n'))
    num_Of_Characters -= num_Of_Num
    desired_Num_Of_Char(num_Of_Characters)
    num_Of_Punc = int(input('\nHow many puncuations would '
                              + 'you like in your password?\n'))
    num_Of_Characters -= num_Of_Punc
    desired_Num_Of_Char(num_Of_Characters)
    t_Pass = password_Generator(num_Of_Lowercase, num_Of_Uppercase, num_Of_Num,
                        num_Of_Punc)
    return t_Pass

def desired_Num_Of_Char(num_Of_Characters):
    if num_Of_Characters < 0:
        print('You went over your desired number of characters\n')
        menu_Two()
    else:
        print(f'You have {num_Of_Characters} left')


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
    menu_Choice = menu_One()
    if menu_Choice == '1':
        t_Pass = password_Generator(3,3,2,2)
    elif menu_Choice == '2':
        t_Pass = menu_Two()
    else:
        print('\nincorrect input:\n')
        menu_One()

    print(f'Your password is: {t_Pass}\n')
    TF = again()
