# lab6_pwgen.py

from random import shuffle
from random import choice
from string import ascii_letters
from string import digits
from string import punctuation

'''
I realize there is no good input validation, will be adding that later!
'''

pw_letters = int(input("\n" + "How many letters would you like in your password? "))
pw_numbers = int(input("\n" + "How many numbers would you like? "))
pw_punct = int(input("\n" + "How much punctuation? "))

password = ''

for num in range(pw_letters):
    password = password + (choice(ascii_letters))
for num in range(pw_numbers):
    password = password + (choice(digits))
for num in range(pw_punct):
    password = password + (choice(punctuation))

password_list = list(password)
shuffle(password_list)
password = ''.join(password_list)

print('\n' + f'Your password is: ' + password)
