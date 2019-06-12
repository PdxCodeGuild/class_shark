## Caleb Mealey - PDX CODE Guild
## Lab 3: Grading
## Let's convert a number grade to a letter grade, using `if` and `elif` statements and comparisons.

# Lab3.Mealey.py
# import sys module
import sys
# input validation
valid = False
while not valid: 
	# get grade from input
	try:
		grade_num = int(input("Enter a number between 0 - 100: "))
		if 0 <= grade_num < 120:
			valid = True
		else:
			raise ValueError
	except ValueError:
		print('Invalid')

# Figure out if the grade is a '+' or '-'
# If the number 100 or greater, add the suffix '+', as that is an A+ grade.
if grade_num // 100 == 1:
	out_suffix = '+'		
elif grade_num % 10 < 3:
	out_suffix = '-'
elif grade_num % 10 > 7:
	out_suffix = '+'
else:
	out_suffix = ''

# Figure out the letter grade, calculated from the inputted integer grade by the user
if 0 <= grade_num < 60:
	letter_grade = 'F'
elif grade_num	< 70:
	letter_grade = 'D'
elif grade_num < 80: 
	letter_grade = 'C'
elif grade_num < 90:
	letter_grade = 'B'
else: 
	letter_grade = 'A'

# Print the grade, if it's an 'F' drop the '+' or '-', as you cannot get either of those suffix for an 'F' grade
if letter_grade == 'F':
	print(letter_grade)
# Print the grade with the suffix, as it is not an F
else:
	print(letter_grade + out_suffix)