import random

def generate(choice):
    v_Eye = ['o', 'O', '0', '\'']
    v_Nose = ['|', 'L', 'o', '1', 'O']
    v_Mouth = ['O', '.', '_', '-']
    one_Line_V_Mouth = ['o', ',', ]
    h_Eye = [':', ';', '|', '[:', ']', 'B']
    h_Nose = ['-', '+', 'O', '>']
    h_Mouth = ['O', 'P', 'p', ')', '(']

    if choice == 1:
        """one-line horizontal faces"""
        eye = random.choice(h_Eye)
        nose = random.choice(h_Nose)
        mouth = random.choice(h_Mouth)
        print('\n' + eye + nose + mouth + '\n')

    elif choice == 2:
        """one-line vertical faces"""
        l_eye = random.choice(v_Eye)
        mouth = random.choice(one_Line_V_Mouth)
        r_eye = random.choice(v_Eye)
        print('\n' + '(' + l_eye + mouth + r_eye + \n')

    elif choice == 3:
        """Multi-line vertical faces"""
        l_H_Eye = random.choice(v_Eye)
        r_H_Eye = random.choice(v_Eye)
        nose = random.choice(v_Nose)
        mouth = random.choice(v_Mouth)
        print('\n' + l_H_Eye + ' ' + r_H_Eye + '\n '
              + nose + '\n ' + mouth + '\n')

    elif choice == 4:
        generate(random.randint(1,3))

    else:
        print('sorry incorrect choice\n')

print("here are five emoticons!")
for a in range(5):
    generate(4)

f_choice = True

while f_choice:
    choice = int(input('what type of emoticon would you like to generate? \n'
                + 'one-line horizontal faces: 1\n'
                + 'one-line vertical faces:   2\n'
                + 'multi-line vertical faces: 3\n'
                + 'suprise me!                4\n'))
    generate(choice)
    f_choice = input('Would you like to make another emoji? y/n ')
    if f_choice == 'y':
        f_choice = True
    elif f_choice == 'n':
        f_choice = False
    else:
        print('Incorrect input: Goodbye!')
        f_choice = False
