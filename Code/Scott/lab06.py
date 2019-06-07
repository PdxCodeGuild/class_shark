"""
Name:           Scott Tran
Date            6/5/2019
Assignment:     Generate a password of length n using a while loop and random.choice
"""

import random
import string

pw_length = int(input("How long of a password would you like?  "))

pw = ''

for i in range(pw_length):
    pw += (random.choice(string.printable))

print(pw)

   