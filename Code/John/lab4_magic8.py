# lab4_magic8.py

from random import choice

predictions = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it",
    "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again, ",
    "Ask again later", "Better not tell you , now""Cannot predict now", "Concentrate and ask again", "Don't count on it",
    "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

print('-' * 75 + '\n')
print("Welcome to the Mysterious Digital Magic 8-ball!!! (please don't shake) =p")
print("You may ask any direct question that results in a yes or no answer!")
print("Remember to say 'done' when you have no further questions of me!")
print('-' * 75 +'\n')

question = ''

while question != 'done':
    question = input("What is the question you most desire answered? ").strip().lower()
    if question == 'done':
        break
    else:
        print('\n' + choice(predictions) + '\n')
