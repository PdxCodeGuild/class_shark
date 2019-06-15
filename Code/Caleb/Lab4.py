# Lab 4: Magic 8-Ball
# Let's write a program to simulate the classic "Magic Eight Ball"

# 1. Print a welcome screen to the user.
# 2. Use the random module's random.choice() to choose a prediction.
# 3. Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
# 4. Display the result of the 8-ball.

# Version 2
# Using a while loop, keep asking the user for a question, if they enter 'done', exit

# import random module
import random

# print welcome screen to user
print('Welcome to the Magic 8 Ball')

# Establish a list of the 8 standards our magic 8 ball can select its answer from
predictions = ['it is certain', 'it is decidly so', 'without a doubt', 'yes, definitely', 'Most likely', 'Ask again later', 'Don\'t count on it', 'Outlook not so good']

# Set the value of the first answer to the user's question to one of the randomly selected predictions from our list of 8 predictions we just established
answer = random.choice(predictions) 
 
# ask the user the first question 
Question = input("Enter a questions for the Magic 8-ball to answer: ")

# extra line for readability
print()

# print the question again for the user
print(Question)

# print the answer for the user
print(answer)

# extra line for readability
print()

# Set the value of the next answer to the user's question to one of the randomly selected predictions from our list of 8 predictions
answer = random.choice(predictions)

# ask the user the second question, allowing them to enter "done" to end their session
Question = input("Enter another question for the Magic 8-ball to answer or enter \"done\" to end your session: ")

# while loop that continues the session by asking a new question if the input given by the user is not equal to "done"
while Question != 'done':
    print(answer)
    print()
    answer = random.choice(predictions)
    Question = input("Enter another question for the Magic 8-ball to answer or enter \"done\" to end your session: ")
 

# print "Goodbye" to the user who entered "done"
print("Goodbye")

# extra line for readability
print()

