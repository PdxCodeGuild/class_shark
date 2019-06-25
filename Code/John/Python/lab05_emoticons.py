# lab05_emoticons.py

import random
print('Welcome to the Emoticon Generator! I hope you enoy!!!')
more = 'y'
eye_list = [':', ';', '8', 'X']
nose_list = ['-', '*', ' ']
mouth_list =['}',')','(','<','D','p','P']
out_string = ''
# more == 'y'
while more == 'y':
    out_string = out_string + (random.choice(eye_list) + random.choice(nose_list) + random.choice(mouth_list))
    out_string = '\n' + out_string + '\n'
    print(out_string)
    more = input('Would you like to generate another emoticon? (y/n) ')
