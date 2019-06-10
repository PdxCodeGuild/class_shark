"""
Name:           Scott Tran
Date            6/7/2019
Assignment:     Write program that allows the user to convert a number between units. Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are inches, feet, yards, miles, meters, and kilometers.
"""


def integer():
    while True:
        try:
            n = int(input("What is the distance? "))
            return n
            break
        except ValueError:
            print("No valid integer! Please try again ...")


def input_unit(x):
    while True:
        unit = str(input("What is the input unit? (inches, ft, yds, mi, m, km): "))
        if unit in ("inches", "ft", "yds", "mi", "m", "km"):
            if unit == 'ft':
                print(f"{x} feet is {round(x*0.3048,1)} meters")
                break
            elif unit == 'inches':
                print(f"{x} inches is {round((x)*0.0254,1)} meters")
                break
            elif unit == 'yds':
                print(f"{x} yards is {round((x)*0.9144,1)} meters")
                break
            elif unit == 'mi':
                print(f"{x} miles is {round((x)*1609.34,1)} meters")
                break
            elif unit == 'm':
                print(f"{x} meters is {x} meters")
                break
            elif unit == 'km':
                print(f"{x} km is {x*1000} meters")
                break
            else: 
                print("You have an error")
        else:
            print(f"{unit} was not one of the selections.") 


input_unit(integer())