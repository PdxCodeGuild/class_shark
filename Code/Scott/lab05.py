"""
Name:           Scott Tran
Date            6/5/2019
Assignment:     Generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth
"""
import random

eyes = [':', ';', '*']
nose = ['-', '>', 'O']
mouth = [')', '(', '\\', '|', '[', '[', 'P']

count = 0

while count < 5:

    print(random.choice(eyes) + random.choice(nose) + random.choice(mouth))
    count += 1