"""
Name:           Scott Tran
Date            6/20/2019
Assignment:     Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

    1) Convert the input string into a list of ints
    2) Slice off the last digit. That is the check digit.
    3) Reverse the digits.
    4) Double every other element in the reversed list.
    5) Subtract nine from numbers over nine.
    6) Sum all values.
    7) Take the second digit of that sum.
    8) If that matches the check digit, the whole card number is valid.

"""


def sixteen():
    
    while True:
        try:
            x = input("Please give me your 16-digit card number. ")
            if len(x) == 16:
                return list(x)
            else:
                print("That isn't a valid string, try again.")
                False
        except:
            print("Error")


def convert(x):
    for i in x:
        card_list.append(int(i))
    return(card_list)


def every_other2(x):
    for i in range(len(x)):
        if i%2 == 0:
            x[i] = x[i]*2
    return x


def over_nine(x):
    for i in range(len(x)):
        if x[i] > 9:
            x[i] = x[i]-9
    return x


def adding(x):
    total = 0
    for i in x:
        total += i
    return total


def check(x):
    if x == y:
        return "Your card is valid."
    else:
        return "Your card is not valid."



card_list = []

x = convert(sixteen())
print(f"1) Your card numbers convert to a list of integers: {x}")

y = x.pop(-1)
print(f"2) Slicing off the last digit creates {x} with the check digit of {y}")

x.reverse()
print(f"3) The reverse list is {x}")

print(f"4) Double every other element: {every_other2(x)}")

print(f"5) Subtract nine from numbers over nine: {over_nine(x)}")

print(f"6) Sum all values is : {adding(x)}")

z = adding(x)
final_num = int(z/10%10)
print(f"7) The second digit of that sum is: {final_num}")

print(f"8) {check(final_num)}")
