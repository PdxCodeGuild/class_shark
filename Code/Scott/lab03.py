"""
Name:           Scott Tran
Date            6/5/2019
Assignment:     Convert a number grade to a letter grade, using if and elif
"""
grade = int(input("What score did you get?  "))

if grade >= 90:
    print("You got an A!")
elif grade >= 80:
    print("You got an B.")
elif grade >= 70:
    print("You got an C..")
elif grade >= 60:
    print("You got an D...")
else:
    print("You failed with an F?")
