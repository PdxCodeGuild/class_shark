# Lab 15: Number to Phrase
# Version 1:
# Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.
# Hint: you can use modulus to extract the ones and tens digit.
# x = 67
# tens_digit = x // 10
# ones_digit == x % 10
# Hint 2: use the digit as an index for the a list OR as a key for a dict of digit: phrase pairs

print('Welcome to Lab 15, a program coded in python by Caleb Mealey')

def menu_one():
    input_num = int(input('Enter a whole integer between 0-99: '))
    TF = True
    while TF:
        if -1 < input_num < 100:
            TF = False
            return input_num
        else:
            input_num = int(input('Invalid Entry. Please enter a valid integer between 0-99: '))


def tens_place(x):
    if x > 20:
        tens = x // 10
        tens_dict = {2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}
        return tens_dict[tens]
    else:
        tens = ''
        return tens


def ones_place(y):
    if y > 20:
        ones = y % 10
        ones_dict = {0:'', 1:'-one', 2:'-two', 3:'-three', 4:'-four', 5:'-five', 6:'-six', 7:'-seven', 8:'-eight', 9:'-nine'}
    elif 10 < y < 20: 
        ones = y
        ones_dict = {11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eightteen', 19:'nineteen'}
    elif y < 10:
        ones = y
        ones_dict = {0:'one', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
    return ones_dict[ones]

my_z =  menu_one()
print(f'{tens_place(my_z)}{ones_place(my_z)}')
print('-' * 60)
