#Lab 05 Random Emoticon Generator
#Step 1 Define a list of eyes
#Step 2 Define a list of noses
#Step 3 Define a list of mouths
#Step 4 Randomly pick a set of eyes
#Step 5 Randomly pick a nose
#Step 6 Randomly pick a mouth
#Step 7 Assemble and display the emoticon

import random
eyes = [':', ';', ':.', '>:', '8']
noses = ['o','-','O', '~']
mouths = ['D',')','P','(']

print(random.choice(eyes) + random.choice(noses) + random.choice(mouths))
