# lab 3 - grading.py

# input validation
valid = False
while not valid:
    # get grade from input
    grade = int(input("Enter a number between 0-100: "))
    if 0 <= grade < 120:
        valid = True
    else:
        print('Invalid')

# figure out if grade is + or -
if grade % 10 < 5:
    out_suffix = '-'
elif grade % 10 > 5:
    out_suffix = '+'
else:
    out_suffix = ''

# figure out letter grade
if 90 <= grade:
    letter_grade = 'A'
elif 80 <= grade:
    letter_grade = 'B'
elif 70 <= grade:
    letter_grade = 'C'
elif 60 <= grade:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# print grade
if letter_grade == 'F':
    # F has no + or -
    # e.g. 19 should not give you an F+
    print(letter_grade)
else:
    print(letter_grade + out_suffix)