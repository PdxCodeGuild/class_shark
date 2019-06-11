"""
Name:           Scott Tran
Date            6/7/2019
Assignment:     Write program that allows the user to convert a number between units. Ask the user for the distance, the starting units, and the units to convert to.
"""


def integer():
    while True:
        try:
            n = int(input("What is the distance? "))
            return n
            break
        except ValueError:
            print("No valid integer! Please try again ...")


def input_unit():
    while True:
        unit = (input("What is the input unit? (ft, mi, m, km): "))
        if unit in ("ft", "mi", "m", "km"):
            return unit
            break
        else:
            print(f"{unit} was not one of the selections. Please try again...")


def output_unit():
    while True:
        unit = (input("What is the output unit? (ft, mi, m, km): "))
        if unit in ("ft", "mi", "m", "km"):
            return unit
            break
        else:
            print(f"{unit} was not one of the selections. Please try again...")


def convert_to_meters(i, u):
    return i * dict_input[u]


def convert_from_meters(i, u):
    return i * dict_output[u]


dict_input = {"ft": 0.3048, "mi": 1609.344, "m": 1, "km": 1000} # Define unit conversion (library) for feet, miles, meters, kilometers ==> meters

dict_output = {"ft": 3.2808398950131, "mi": 0.00062137119223733, "m": 1, "km": 0.001}

x = integer()
y = input_unit()
z = output_unit()
a = convert_from_meters(convert_to_meters(x,y),z)

print(f"{x}{y} is {a}{z}")