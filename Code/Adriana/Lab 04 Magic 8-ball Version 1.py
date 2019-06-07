#LAB 4 MAGIC 8-BALL
#Step 1 Print a welcome screen to the user.
#Step 2 Use the random module's random.choice() to choose a prediction.
#Step 3 Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
#Step 4 Display the result of the 8-ball.

import random
import time
print('Welcome to the Magic 8-Ball')
#wait for 2 seconds
time.sleep(2)
user_question = input ("Ask me any Question!: ")
lottery_list = ['It is certain', 'It is decidedly so','Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes','Reply hazy try again','Ask again later','Better not tell you now','Cannot predict now','Concentrate and ask again','Dont count on it','My reply is no','My sources say no','Outlook not so good','Very doubtful']
print(f"{random.choice(lottery_list)}")
