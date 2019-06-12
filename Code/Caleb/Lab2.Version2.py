## Lab 2: Mad Libs

## Write a simple program that prompts the user for several ## inputs then
## prints a [Mad Lib](https://en.wikipedia.org/wiki/Mad_Libs) as the result.

## Version 2: 
## Make a functional solution that utilizes lists. For example, ask the user for 3 adjectives, separated by commas, then use the .split() function to store each adjective and later use it in your story.
## Add randomness! Use the random module, rather than selecting which adjective goes where in the story.
import random

input_verb_list = []
input_verb_list = (input('Enter 3 adjectives, separated by commas: '))
input_verb_list = input_verb_list.split(', ')
print(input_verb_list)

print('You and your ' + random.choice(input_verb_list) + ' best friend walked into a bar. Before either of you could stop and locate an open table or place at the bar, a ' + random.choice(input_verb_list) + ' being of light approached you both, and in a booming voice said, \"You both are lost, you must learn to be more than ' + random.choice(input_verb_list) + ' members of this earth or you shall both perish!\" You quickly arise from bed, and realize it was all just a dream.')