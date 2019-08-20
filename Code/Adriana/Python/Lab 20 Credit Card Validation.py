#LAB 20
#Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

#Convert the input string into a list of ints
#Slice off the last digit. That is the check digit.
#Reverse the digits.
#Double every other element in the reversed list.
#Subtract nine from numbers over nine.
#Sum all values.
#Take the second digit of that sum.
#If that matches the check digit, the whole card number is valid.


creditcard_input = input(f'Enter Credit Card Number: ')
    #this is what number they enter

new_number = list(map(int,creditcard_input))
    #this is converting the string to a list of integers
print(f'You entered: {creditcard_input}')

short_num = new_number[:-1]
    #this is the list without the end number
print(f'Your Credit Card Number Shortened: {short_num}')
    #print(short_num)

check_digit = new_number[-1]
    #this is the last number on the original list
    #print(check_digit)
print(f'This is your check digit: {check_digit}')

reverse_short = short_num[::-1]
print(f'These are the digits reversed: {reverse_short}')
    #print(reverse_short)

print("Now run 'validate()' to check if this credit card is valid")

def validate():

    for i in range(0, len(reverse_short), 2):
        reverse_short[i] *= 2
    print(reverse_short)

    for i in range(len(reverse_short)):
        if reverse_short[i] > 9:
            reverse_short[i] -= 9
    print(reverse_short)

    total_cc = sum(reverse_short)%10
    print(total_cc)

    print(f'You entered: {creditcard_input}')
    print(f'Your Check Digit is {check_digit}')

    if (total_cc) == check_digit:
        print(f'VALID!')
    else:
        print(f'NOT VALID')