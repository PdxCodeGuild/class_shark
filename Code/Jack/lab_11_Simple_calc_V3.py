
def run_Eval():
    while True:
        usr_eq = input('\nPlease enter your equation: ')
        try:
            sol = eval(usr_eq)
            break
        except:
            print('improper input: ')
    return sol


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def divide(num1, num2):
    try:
        t_num1 = float(num1)
        t_num2 = float(num2)
        sum = t_num1/t_num2
    except ZeroDivisionError:
        print('\nCan\'t divide by Zero')
    else:
        return sum


def mult(num1, num2):
    return num1 * num2


def power(num1, num2):
    return num1**num2


l_valid_Inputs = ['+', '-', '/', '*', '**', 'adv', 'done']

print('welcome to Simple Calc!')
TF = True
while TF:
    TF_Menu = True
    while TF_Menu:
        print('What operation would you like to perform?')
        usr_Choice = input('You may choose from the following: \n'
            + '+, -, /, *, or ** (pwr of)\n'
            + '\'adv\' (to enter a full arithmaetic expression)\n'
            + 'or \'done\' to \n')
        if usr_Choice.strip() not in l_valid_Inputs:
            print('Invalid input: ')
        elif usr_Choice == 'done':
            TF = False
            TF_Menu = False
        elif usr_Choice == 'adv':
            print('\nYour answer is:', run_Eval(), '\n')
        else:
            TF_Menu = False

    if TF:
        while True:
            try:
                usr_Num_One = int(input('First number: '))
            except ValueError:
                print('invalid input: ')
            else:
                break

    if TF:
        while True:
            try:
                usr_Num_Two = int(input('Second number: '))
            except ValueError:
                print('invalid input: ')
            else:
                break

    if TF:
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
        print('\nYour answer is:', sol, '\n')
