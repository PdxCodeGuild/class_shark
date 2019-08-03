# lab 8

# Version 1 
unsorted_amount = input("Type the total number of pennies for the dollar amount. \n For example, $1.36 would be 136:  ")
quarters = int(unsorted_amount) // 25
dimes = int(unsorted_amount) // 10
nickels = int(unsorted_amount) // 20
pennies = int(unsorted_amount) // 100

total_amount = (f"you have {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies.")
print(total_amount)

# Version 2 Convert a float to integer, example converting $1.36 to 136 pennies
dollar_amount = input("Type a dollar amount to convert to pennies. For example, 10.57:  ")
pennies = float(dollar_amount) * 100
total_pennies = int(pennies)

print(total_pennies)
