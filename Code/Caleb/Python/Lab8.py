## Lab 8: Make Change
## Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. Always break the total into the highest coin value first, resulting in the fewest amount of coins. For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

## Concepts Covered:
##      - conditionals, comparisons
##      - arithmetic

## Version 1:
##      Have the user enter the total number in pennies, eg for $1.36, the user will enter 136

## Version 2:
##      Have the user enter a dollar amount (1.36), convert this to the total in pennies

# Display Welcome Screen
print('Welcome to the Make Change Lab - developed by Caleb Mealey in Python')

# Extra line for readability
print()

# Prompt the user for a number of pennies, assign this inputted value to the variable, 'total_to_be_changed'
total_to_be_changed = int(input('Enter the total number of pennies you would like converted into change or dollars: '))

# Convert the pennies into dollars
dollars = float(total_to_be_changed // 100)
remainding_change = float(total_to_be_changed % 100)*.01

## Test Prints, used while developing to check code
## print(dollars)
## print(remainding_change)

print('The total counted & changed amount is: $', end='') 
print(dollars + remainding_change)

# Little side fun on how to break down a total pennies amount into quarters, dimes, nickels, and remainding pennies
# Convert the remainding pennies into quarters
# quarters = total_to_be_changed // 25
# total_to_be_changed = total_to_be_changed - (25 * quarters)

# Convert the remainding pennies into dimes
# dimes = total_to_be_changed // 10
# total_to_be_changed = total_to_be_changed - (10 * dimes)

# Convert the remainding pennies into nickels
# nickels = total_to_be_changed // 5
# total_to_be_changed = total_to_be_changed - (5 * nickels)

# print('The total amount you entered is: $' + str(dollars) + ' dollar(s) & ' + str(quarters) + ' quarter(s), & ' + str(dimes) + ' dime(s), & ' + str(nickels) + ' nickel(s), & ' + str(total_to_be_changed) + ' penny')


## Version 2:
##      Have the user enter a dollar amount (1.36), convert this to the total in pennies

# Prompt the user to enter a dollar amount. End the prompt with $ so the user know to type a number.
total_dollars = float(input('Now enter a dollar amount (i.e. $3.77), and I will conver this to the total in pennies: $'))

# convert the inputted floated input dollar amount into total pennies, by first separating the change from the dollars and then multiplying each by 100
total_changed_pennies = int(((total_dollars // 1) + (total_dollars % 1)) * 100)

# Display the generated total amount of pennies converted from the inputted dollar amount
print('$' + str(total_dollars) + ' = ' + str(total_changed_pennies) + ' total pennies')
