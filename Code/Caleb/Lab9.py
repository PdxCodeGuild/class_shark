# Lab 9: Unit Converter
#  This lab will involve writing a program that allows the user to convert a number between units.
# Version 1
#  Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.
##      > what is the distance in feet? 12
##      > 12 ft is 3.6576 m
# Version 2
#   Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.
##      1 ft is 0.3048 m
##      1 mi is 1609.34 m
##      1 m is 1 m
##      1 km is 1000 m
##     Below is some sample input/output:
##      > what is the distance? 100
##      > what are the units? mi
##      > 100 mi is 160934 m
#  Version 3
#   Add support for yards, and inches.
##      1 yard is 0.9144 m
##      1 inch is 0.0254 m

print('Welcome to the Unit Converter Lab, programmed in python by Caleb Mealey')

feet_input = int(input('Enter the number of feet you would like converted into equivalent distance in meters: '))

meters_calc = feet_input * 0.3048

print(str(feet_input) + ' feet is equals to ' + str(meters_calc) + 'meters')

def unit_check(unit_input):
    TF = False
    while not TF:
        if unit_input == 'feet':
            return 0.3048
            TF = True
        elif unit_input == 'miles':
            return 1609.34
            TF = True
        elif unit_input == 'meters':
            return 1
            TF = True
        elif unit_input == 'kilometers':
            return 1000
            TF = True
        else:
            print('Invalid Entry. Please enter a valid unit (feet, miles, meters, or kilometers)')
            custom_distance_unit_type = input('Now enter the unit of distance you would like converted into feet. The acceptable units are: feet, miles, meters, and kilometers: ')

custom_distance_unit_type = input('Now enter the unit of distance you would like converted into feet. The acceptable units are: feet, miles, meters, and kilometers: ')

unit_check(custom_distance_unit_type)

custom_distance_original = input('Enter the amount of ' + str(custom_distance_unit_type) + ' you would like converted into meters: ')

calc_distance = int(custom_distance_original) * int(unit_check(custom_distance_unit_type))

print(str(custom_distance_original) + str(custom_distance_unit_type) + 'is equal to ' + str(calc_distance) + ' meters')