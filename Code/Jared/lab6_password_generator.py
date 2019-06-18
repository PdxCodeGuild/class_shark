# lab 6 password generator
import random
import string




#Version 2
chr_list = string.ascii_letters + string.digits + string.punctuation
pass_length = int(input("How long would you like your password to be?: 'Enter any number'"))

password = ''

for i in range(pass_length):
    password += random.choice(chr_list)
print(password) #how do i print for loop on one line a different way?
