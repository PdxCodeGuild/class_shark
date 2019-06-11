# lab8_make_change.py
print("-" * 80)
print("Let's convert your dollars to change!!! " + '\n')

invalid = True
while invalid:
    dollar_amount = float(input("How much money do you have? Remeber the correct decimal place please!! :"))
    if dollar_amount %1 != 0:
        invalid = False

dollar_amount *= 100
dollar_amount = int(dollar_amount)
pennies = dollar_amount

quarters = pennies // 25
pennies %= 25

dimes = pennies // 10
pennies %= 10

nickles = pennies // 5
pennies %= 5

print("\n" + f"Your money converted to change is {quarters} quarters, {dimes} dimes, {nickles} nickles, {pennies} pennies!")
print("-" * 80)
