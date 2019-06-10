import random

class Eight_Ball():
    """docstring Eight_Ball"""

    eight_Ball_Choices = [
        'It is certain'
        ,'It is decidedly so'
        ,'Without a doubt'
        ,'Yes definitely'
        ,'You may rely on it'
        ,'As I see it, yes'
        ,'Most likely'
        ,'Outlook good'
        ,'Yes'
        ,'Signs point to yes'
        ,'Reply hazy try again'
        ,'Ask again later'
        ,'Better not tell you now'
        ,'Cannot predict now'
        ,'Concentrate and ask again'
        ,'Don\'t count on it'
        ,'My reply is no'
        ,'My sources say no'
        ,'Outlook not so good'
        ,'Very doubtful'
]

    def __init__(self):
        print("Welcome to the Mystical Magical Monotonous Eyate Ball")

    def ask_Question(self):
        question = input('Ask the Eyate Ball a question: \n(\'done\' to exit) \n')
        if question != 'done':
            print(f'\n{random.choice(self.eight_Ball_Choices)}\n')
            self.ask_Question()
        # self.another_Question()

    # def another_Question():
        # choice = input('Would you like to ask another question? y/n')
        # if choice == 'y':
            # self.ask_Question()
        # elif choice == 'n':
            # print('thank you, please leave a donation in the box')
        # else:
            # print('Incorrect input')
            # self.another_Question()




ball = Eight_Ball()
ball.ask_Question()
