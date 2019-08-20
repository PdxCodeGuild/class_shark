#LAB 09
#Step 1 Ask the user for the number of feet, and print out the equivalent distance in meters.

import time
print("Welcome to Unit Conversion")
#wait 2 seconds before asking question
time.sleep(2)

select_feet = int(input("How many feet would you like to convert to meters? "))
meters_output = select_feet * 0.3048
print(f"{select_feet} feet is {meters_output} meters")
