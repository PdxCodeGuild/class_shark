"""
Name:           Scott Tran
Date            6/5/2019
Assignment:     Write a program to simulate the classic "Magic Eight Ball"
"""
import random

print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Welcome to the Magic 8 Ball, Let us tell your future......")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

fortune = ['It is certain',
'It is decidedly so',
'Without a doubt',
'Yes definitely',
'You may rely on it',
'As I see it, yes',
'Most likely',
'Outlook good',
'Yes',
'Signs point to yes',
'Reply hazy try again',
'Ask again later',
'Better not tell you now',
'Cannot predict now',
'Concentrate and ask again',
'Don\'t count on it',
'My reply is no',
'My sources say no',
'Outlook not so good',
'Very doubtful'
]

Play = True

while Play: 
    ask = input("\nWhat question can we answer?   ")


    print("The magic 8 Ball says... " + random.choice(fortune))

    again = input("\nWould you like to ask again? please type 'yes' or 'no':  ")
    if again == "no":
        Play = False