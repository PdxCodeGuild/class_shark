# lab03_grading.py
print('\nBy inputing your number grade you will see what your letter grade is.\n')
user_input = input('What is your number grade? >> ')
user_input = int(user_input)
user_input % 10
if user_input % 10 < 5:
    out_suffix = '-'
elif user_input % 10 > 5:
    out_suffix = '+'
else:
    out_suffix = ''
if user_input > 100 or user_input < 0:
    print(f'Invalid input, please try again.' )
elif user_input >= 90:
    print(f'Your letter grade: A {out_suffix}')
elif user_input >= 80:
    print(f'Your letter grade: B {out_suffix}')
elif user_input >= 70:
    print(f'Your letter grade: C {out_suffix}')
else:
    print("Sorry, you will have to take this course again...")
