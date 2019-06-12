input string


l_valid_Inputs = ['+', '-', '/', '*', '**', 'adv', 'done']

print('welcome to Simple Calc!')
TF = True
while TF:
    TF_Menu = True
    while TF_Menu:
        print('What operation would you like to perform?')
        usr_Choice = input('You may choose from the following: \n'
            + '+, -, /, *, or ** (pwr of)\n'
            + 'adv (to enter a full arithmaetic expression)\n'
            + 'done\n')
        if usr_Choice.strip() not in l_valid_Inputs:
            print('Invalid input: ')
        elif usr_Choice == 'done':
            TF_Menu = False
        elif usr_Choice == 'adv':
            run_Eval()


    TF_First_Num = True
    while TF_First_Num:
        try:
            usr_Num_One = int(input('First number: '))
        except ValueError:
                    print('invalid input: ')
        else:
            TF_First_Num = False

    TF_Second_Num = True
    while TF_Second_Num:
        try:
            usr_Num_Two = int(input('Second number: '))
        except ValueError:
            print('invalid input: ')
        else:
            TF_Second_Num = False


    if usr_Choice == '+':
        sol = add(usr_Num_One, usr_Num_Two)
    elif usr_Choice == '-':
        sol = subtract(usr_Num_One, usr_Num_Two)
    elif usr_Choice == '/':
        sol = divide(usr_Num_One, usr_Num_Two)
    elif usr_Choice == '*':
        sol = mult(usr_Num_One, usr_Num_Two)
    elif usr_Choice == '**':
        sol = power(usr_Num_One, usr_Num_Two)
