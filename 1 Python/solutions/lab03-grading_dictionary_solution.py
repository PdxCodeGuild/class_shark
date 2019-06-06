# lab 3 - grading_dictionary_solution.py

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

# dictionary solution
# set range as keys and letter grades as values
grades = {
    range(90, 101): 'A',
    range(80, 90): 'B',
    range(70, 80): 'C',
    range(60, 70): 'D',
    range(0, 60): 'F'
}

# loop over the keys in grades
for grade_range in grades:
    # check if grade is in that range
    if grade in grade_range:
        # pass in the key range to get the letter grade val
        letter_grade = grades[grade_range]
        if letter_grade == 'F':
            # F has no + or -
            # e.g. 19 should not give you an F+            
            print('F')
        else:
            print(letter_grade + out_suffix)
        break