# lab11_simple_calc.py

import string
operators = ("+", "-", "*", "/", "done")

print("-" * 109)
print(f"Welcome to the Simple Calculator, I can do the following arithmatic operators: {operators} ")

invalid_operator = True

while invalid_operator:
    user_operation = input("\n" + "Which arithmatic operation would you like to perform? ").lower().strip()
    if user_operation not in operators:
        print("\n" + "Please select a valid operator.")
    elif user_operation in operators:
        if user_operation == "done":
            print("\n" + "Goodbye!!")
            print("-" * 109)
            break   # using break as instructions said to
        else:
            num1 = None
            num2 = None
            print("\n")
            while num1 is None:
                try:
                    num1 = float(input("what is your first number? "))
                except ValueError:
                    print("\n" + "Invalid input, please try again. ")
            while num2 is None:
                print("\n")
                try:
                    num2 = float(input("what is your second number? "))
                except ValueError:
                    print("\n" + "Invalid input, please try again. ")
            if user_operation == '+':
                print("\n" + f"{num1} + {num2} = {num1 + num2}")
            elif user_operation == '-':
                print("\n" + f"{num1} - {num2} = {num1 - num2}")
            elif user_operation == '*':
                print("\n" + f"{num1} * {num2} = {num1 * num2}")
            elif user_operation == '/':
                print("\n" + f"{num1} / {num2} = {num1 / num2}")
