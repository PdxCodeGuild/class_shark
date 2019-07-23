# Lab 6: Password Generator
#   Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters.
# Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.
# Concepts Covered
#   input, print
#   looping
#   random.choice
#   the 'string builder pattern'
# Version 2
#   Allow the user to enter the value of n, remember to convert its type, as input returns a string.
# Version 3 (optional)
# Ask the user for how many lowercase letters, uppercase letters, numbers, and special characters they'd like in their password. Generate a password accordingly.

# import random module
import random
# import string module
import string

# Print Welcome Screen
print("Welcome to the Password Generator Practice Lab")
# Establish our list of potential characters from the string module for ASCII Letters, Digits, & Punctuation
all_characters = string.ascii_letters + string.digits + string.punctuation
# split the string of potential characters declared above into an indexed list
all_characters.split

# define a function 'password_generator', which asks for one parameter, n, which is the lengeth of the desired custom password
def password_generator(length):
# Establish a variable 'first_pw', assign it to be an empty list
    first_pw = []
# while loop to iterate through the number of inputted characters to our 'first_pw' list
    while length > 0:
        first_pw.append(random.choice(all_characters))
        length -= 1
# shuffle the 'custom_pw' list
    random.shuffle(first_pw)
# convert the 'custom_pw' list into a string
    first_pw = ''.join(first_pw)
    return first_pw

def password_generator_advanced(lower_num, upper_num, digit_num, punc_num):
# Establish a variable 'custom_pw', assign it to be an empty list
    custom_pw = []
# while loop to iterate through the number of inputted lowercase letters to our 'custom_pw' list
    while lower_num > 0:
        custom_pw.append(random.choice(string.ascii_lowercase))
        lower_num -= 1
# while loop to iterate through the number of inputted uppercase letters to our 'custom_pw' list
    while upper_num > 0:
        custom_pw.append(random.choice(string.ascii_uppercase))
        upper_num -= 1
# while loop to iterate through the number of inputted digits characters to our 'custom_pw' list
    while digit_num > 0:
        custom_pw.append(random.choice(string.digits))
        digit_num -= 1
# while loop to iterate through the number of inputted punctuation characters to our 'custom_pw' list
    while punc_num > 0:
        custom_pw.append(random.choice(string.punctuation))
        punc_num -= 1
# shuffle the 'custom_pw' list
    random.shuffle(custom_pw)
# convert the 'custom_pw' list into a string
    custom_pw = ''.join(custom_pw)
    return custom_pw

# Establish a menu_check variable to be true. Will be used to confirm validity of user inputs
# menu_check1=True
# Declare a menu_check variable to be false, this will be used to validate the input from the user in the second menu for the advanced password
# menu_check2=False

# define a function 'menu_check_one' to confirm the input from the user is valid
def menu_check_one():
    menu_check1 = True
    first_pw_length = int(input("Please enter the desired length of your first custom pseudo-random password: "))
    if first_pw_length > 0:
        menu_check1 = False
        menu_check2 = True
    else:
        print('Invalid Entry. You must enter a positive integer.')
        first_pw_length = int(input("Please enter the desired length of your first custom psuedo-random password: "))
    print('Your first pseudo-random password is: ' + password_generator(first_pw_length))
    menu_check_two()

def menu_check_two():
    print('Now, let\'s create an advanced password. We will allow you to have more control over the quantity of each type of character to be included in your custom password.')
    lowercase_input_num = int(input('Enter the number of lowercase letters you would like in your psuedo-random custom password: '))
    uppercase_input_num = int(input('Enter the number of uppercase letters you would like in your pseudo-random custom password: '))
    digit_input_num = int(input('Enter the number of digits you would like in your pseudo-random custom password: '))
    punc_input_num = int(input('Enter the number of punctuation characters you would like in your pseudo-random custom password: '))
    while menu_check2:
        if lowercase_input_num >= 0 or uppercase_input_num >= 0 or digit_input_num >= 0 or punc_input_num >= 0:
            print('Your custom pseudo-random password is:')
            print(password_generator_advanced(lowercase_input_num, uppercase_input_num, digit_input_num,punc_input_num))
            menu_check2 = False
        else:
            print('Invalid entries. Please reenter valid integers, 0 or greater.')

menu_check_one()