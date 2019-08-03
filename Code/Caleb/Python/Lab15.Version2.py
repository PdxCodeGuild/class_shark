# Lab 15: Number to Phrase
# Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.
# Hint: you can use modulus to extract the ones and tens digit.
# x = 67
# tens_digit = x // 10
# ones_digit == x % 10
# Hint 2: use the digit as an index for the a list OR as a key for a dict of digit: phrase pairs

# Version 2
# Handle numbers from 100-999.

print('Welcome to Lab 15, a program coded in python by Caleb Mealey')

def menu_one(): 
    input_num = int(input('Enter a whole integer between 100-999: '))
    TF = True
    while TF:
        if 99 < input_num < 1000:
            TF = False
            return input_num
        else:
            input_num = int(input('Invalid Entry. Please enter a valid integer between 100-999: '))


def hundreds_place(u):
    hund_dict = {1:'one hundred', 2:'two hundred', 3:'three hundred', 4:'four hundred', 5:'five hundred', 6:'six hundred', 7:'seven hundred', 8:'eight hundred', 9:'nine hundred'}
    hundreds = u // 100
    return hund_dict[hundreds]


def tens_place(x):
    tens = (x - ((x // 100)*100)) // 10
    if x > 1:
        tens_dict = {2:'and twenty', 3:'and thirty', 4:'and forty', 5:'and fifty', 6:'and sixty', 7:'and seventy', 8:'and eighty', 9:'and ninety'}
        return tens_dict[tens]
    else:
        tens = ''
        return tens


def ones_place(y):
    ones = (y % 100)
    if 10 < ones < 20:
        ones_dict = {11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eightteen', 19:'nineteen'}
    elif y < 10:
        ones_dict = {0:'one', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
    else:
        ones = ones % 10
        ones_dict = {0:'', 1:'-one', 2:'-two', 3:'-three', 4:'-four', 5:'-five', 6:'-six', 7:'-seven', 8:'-eight', 9:'-nine'}
    return ones_dict[ones]


my_z =  menu_one()
print(f'{hundreds_place(my_z)} {tens_place(my_z)} {ones_place(my_z)}')
print('-' * 60)
