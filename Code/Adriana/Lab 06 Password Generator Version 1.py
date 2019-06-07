#LAB 06 RANDOM PASSWORD
#Step 01 Generate a password of length n using a while loop and random.choice
#Topics covered: input, print, looping, random.choice, the 'string builder pattern'

import random
import string
password_length = int(input('How many characters would you like your password to be?'))
alphabet_list = string.ascii_lowercase

password_selection = ''

#for loop
for num in range(password_length):
    password_selection = password_selection + random.choice(alphabet_list)
print(password_selection)
