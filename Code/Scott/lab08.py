"""
Name:           Scott Tran
Date            6/6/2019
Assignment:     Convert a dollar amount into a number of coins
"""

coin = int(input("What is the dollar amount?"))

print("\nIn your purse:")

quarters = int(coin//25)
dimes = int((coin - (quarters*25))//10)
nickels = int((coin - (quarters*25)-(dimes*10))//5)
pennies = int((coin - (quarters*25)-(dimes*10)-(nickels*5)))

print(f"there are {quarters} quarter(s),")
print(f"there are {dimes} dime(s),")
print(f"there are {nickels} nickel(s),")
print(f"and there are {pennies} penny(s).")