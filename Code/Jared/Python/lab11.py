#lab 11

def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


print('-' * 65)

print("""Welcome to the Simple Calculator.
You can add, subtract, multiply, and divide.
When finished enter 'done.'""")


while True:
# user chooses the operator
    print('-' * 65)
    operator = input('Choose an operation: +, - , *, or /\n')
    #user chooses first num
    if operator == 'done':
        break

    user_num1 = float(input('Enter a number: '))

    #user chooses second number
    user_num2 = float(input('Enter a number: '))

    if operator == '+':
        print(f"{user_num1} {operator} {user_num2} =", add(user_num1, user_num2))
    elif operator == '-':
        print(f"{user_num1} {operator} {user_num2} =", subtract(user_num1, user_num2))
    elif operator == '*':
        print(f"{user_num1} {operator} {user_num2} =", multiply(user_num1, user_num2))
    elif operator == '/':
        print(f"{user_num1} {operator} {user_num2} =", divide(user_num1, user_num2))
    else:
        print('Invalid')

print("Shutting down.")
print('-' * 65)
