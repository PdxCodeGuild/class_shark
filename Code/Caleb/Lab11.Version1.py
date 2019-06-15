# Lab 11: Simple Calculator

# Version 1:
# Let's write a simple REPL (read evaluate print loop) calculator that can handle addition, subtraction, multiplication, and division. Ask the user for an operator and each operand. Don't forget that input returns a string, which you can convert to a float using float(user_input) where user_input is the string you got from input. Below is some sample input/output.

# Import the operator module, used later to convert the user inputted operand into a executable operation
import operator

# Display Welcome Screen
print('Welcome to the Simple Calculator Lab, coded in python by Caleb Mealey. This Simple Calculator can only perform one calculation at a time.')

# Define a function, 'operand', used to prompt an input from the user for the desired operand to be used in the calculation
def operand():
    TF = False
    operands = ['+', '-', '*', '/']
    operand_input = input('What is the operation you\'d like to perform? ')
    while not TF:
        if operand_input in operands:
            return operand_input
            TF = True
        else:
            operand_input = input('Invalid Entry. Please enter a valid operand for the arithmetic operation you would like to execute. Valid options are: +, -, *, / ')

# Define a function, 'first_int', to prompt the user for a number. Confirm the input is a valid number, with or without decimals, and convert that number into a float integer.
def first_int():
    TF = True
    while TF:
        first_num_input = input('What is the first number? ')
        try:
            first_num_input = float(first_num_input)
            TF = False
            return first_num_input
        except ValueError:
            print('Invalid Entry. Please enter a valid integer or valid number without any letters or punctiation: ')

# Define a function, 'second_int', to prompt the user for a number. Confirm the input is a valid number, with or without decimals, and convert that number into a float integer.
def second_int():
    TF = True
    while TF:
        second_num_input = input('What is the first number? ')
        try:
            second_num_input = float(second_num_input)
            TF = False
            return second_num_input
        except ValueError:
            print('Invalid Entry. Please enter a valid integer or valid number without any letters or punctiation: ')


# Define a function, 'math_calc', which can be used to convert the user inputted operand, along with the two valid user inputted numbers, and return the indicated calculation
def math_calc(num_one, num_two, calc_operand):
    if calc_operand == '+':
        return operator.add(num_one, num_two)
    elif calc_operand == '-':
        return operator.sub(num_one, num_two)
    elif calc_operand == '*':
        return operator.mul(num_one, num_two)
    elif calc_operand == '/':
        return operator.truediv(num_one, num_two)
    else:
        print('We\'re having techinical difficulties and cannot complete your requested calculation. Please try again later.' )

# Declare unique variables to call into action the three functions
a = first_int()
b = operand()
c = second_int()

# Print the user inputted calculation with its solution
print(f'{a} {b} {c} = {math_calc(a, c, b)}')

