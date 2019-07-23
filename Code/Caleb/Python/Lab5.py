# Lab 5: Random Emoticon Generator
# Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth. Examples of emoticons are :-D =^P and :\

# Version 2
# Use a loop to generate 5 emoticons.

## import random
import random
# 1. Define a list of eyes
eyes = [':', ';', '^ ^', '..']
# 2. Define a list of noses
noses = ['<', '>', '^', '.', ',']
# 3. Define a list of mouths
mouths = ['b', ')', '(', 'p']

# define a function named "rand_emoticon_print" with a parameter of "x", which defines how many times you would like to have the random emoticon generator to loop
def rand_emoticon_print(x):
    # begin while loop
    while x > 0:
# 4. Randomly pick a set of eyes, assign the result to variable 'rand_eyes'
        rand_eyes = random.choice(eyes)
# 5. Randomly pick a nose, assign the result to variable 'rand_nose'
        rand_nose = random.choice(noses)
# 6. Randomly pick a mouth, assign the result to variable 'rand_mouth'
        rand_mouth = random.choice(mouths)
# 7. Assemble and display the emoticon, assign the value of the concantenation of the three random eye, nose, & mouth variables to 'final_print'
        final_print = rand_eyes + rand_nose + rand_mouth

# display the assembled emoticon
        print(final_print) 

# add line for readability
        print()

# Minus 1 from x
        x -= 1


# test print
rand_emoticon_print(5)