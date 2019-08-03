"""
Name:           Scott Tran
Date            6/18/2019
Assignment:     Convert a given number (1-999) into its english representation. 
"""


ones = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"} 
teens = {0: "ten", 1: "eleven", 2: "twelve", 3: "Thirteen", 4: "forteen", 5: "fifteen", 6: "sixteen", 7: "seventeen", 8: "eighteen", 9: "nineteen"}

tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

def integer():
    while True:
        try:
            n = int(input("Please give me a number between 1 and 999 to translate: "))
            if n > 0 and n < 1000: 
                return n
            else:
                print("That is not a number in range.", end =" ")
                False
        except ValueError:
            print("No valid integer! Please try again ...")


def num(x):

    if x < 10:
        return ones[x]
    elif x > 9 and x < 20:    
        teens_num = x%10
        return teens[teens_num]
    elif x >19 and x < 100:
        tens_num = x//10
        ones_num = x%10
        return tens[tens_num] + "-" + ones[ones_num]
    else:
        return 'error'


def hundred(x):

    if x > 99 and x < 1000:
        hund_num = x//100
        hund_remain = x%100
        return ones[hund_num] + " hundred and "+ num(hund_remain)
    else:
        return ''


xx = integer()

if xx < 100:
    print(f"The english representation of that number is {num(xx)}.")
else: 
    print(f"The english representation of that number is {hundred(xx)}.")