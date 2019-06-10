#LAB 08 Make Change
#Step 1 Convert a dollar amount into a number of coins.
#Step 2 Outpul will be total number of quarters, dimes, nickles

total_amt = int(input("How many pennies?: "))

quarters = total_amt // 25
total_amt -= quarters*25

dimes = total_amt // 10
total_amt -= dimes*10

nickles = total_amt // 5
total_amt -= nickles*5


print (f"{quarters} quarters")
print (f"{dimes} dimes")
print (f"{nickles} nickles")
print (f"{total_amt} pennies")
