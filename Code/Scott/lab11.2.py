"""
Name:           Scott Tran
Date            6/7/2019
Assignment:     Write a simple REPL (read evaluate print loop) calculator that can handle addition, subtraction, multiplication, and division. Ask the user for an operator and each operand. Allow the user to keep performing operations until they say 'done'
"""


def operation():
    while True:
        x = input("What is the operation you'd like to perform? Please choose from (+, -, *, /) or type 'done' to quit. ")
        if x in ("+", "-", "*", "/"):
            return x
        elif x == "done":
            quit()
        else:
            print(f"{x} was not one of the selections. Please try again...") 


def first_num():
    while True:
        x = input("What is the first number? ")
        if x.isdigit():
            return x
        elif x == "done":
            quit()
        else:
            print(f"{x} was not an integer number. Please try again...") 


def second_num():
    while True:
        x = input("What is the second number? ")
        if x.isdigit():
            return x
        elif x == "done":
            quit()
        else:
            print(f"{x} was not an integer number. Please try again...") 

while True:
    x = operation()
    y = first_num()
    z = second_num()
    a = int(y) + int(z)

    print(f"{y} {x} {z} = {a}")
