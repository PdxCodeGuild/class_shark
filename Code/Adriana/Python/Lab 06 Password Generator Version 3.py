#LAB 06 RANDOM PASSWORD
#Step 01 Generate a password of length n using a while loop and random.choice
#Topics covered: input, print, looping, random.choice, the 'string builder pattern'

#Version 3 (optional)
#Step 1 Ask the user for how many lowercase letters, uppercase letters, numbers, and special characters they'd like in their password.
#Step 2 Generate a password accordingly.

import random
import string
alphabet_list = string.ascii_lowercase
bigalphabet_list = string.ascii_uppercase
num_list = string.digits
spec_list = String.isalnum

lower_case = int(input('How many lowercase letters: '))
upper_case = int(input('How many uppercase letters: '))
numbers = int(input('How many numbers: '))
special_char= int(input('How many special characters: '))

total_length = lower_case + upper_case + numbers + special_char

for num in range(total_length):
total_length = total_length + random.choice(alphabet_list) + random.choice(bigalphabet_list) + random.choice(num_list) + random.choice(spec_list)
print (total_length)

#password_selection = ''

#for loop
#for num in range(password_length):
#    password_selection = password_selection + random.choice(alphabet_list)
#print(password_selection)
