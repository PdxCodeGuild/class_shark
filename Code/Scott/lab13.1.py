"""
Name:           Scott Tran
Date            6/11/2019
Assignment:     Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string.
"""

import string

alpha = dict(zip(string.ascii_lowercase, range(0,26)))
num = dict(zip(range(0,26),string.ascii_lowercase))  


message = input("Enter your secret word.  ")


cypher = []
secret_word = ""

for i in message.lower():
    if alpha[i] + 13 < 26:
        cypher.append(int(alpha[i]) + 13)
    else:
        cypher.append(int(alpha[i]) - 13)

print("The secret word has been encrypted to: ")      
for i in cypher:
    print(num[i], end= "")
print("\n")    