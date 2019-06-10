"""
Name:           Scott Tran
Date            6/7/2019
Assignment:     Write program that allows the user to convert a number between units. Ask the user for the number of feet, and print out the equivalent distance in meters
"""


def integer():
    while True:
        try:
            n = int(input("What is the distance in feet? "))
            print(f"{n} feet is {round(n*0.3048,1)} meters")
            break
        except ValueError:
            print("No valid integer! Please try again ...")


integer()
