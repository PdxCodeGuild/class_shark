#LAB 3 - Grading
#Step 1 Have the user enter a number representing the grade (0-100)
#Step 2Convert the number grade to a letter grade

#int used to convert string input to an integer

user_score = int(input("What was your number grade? "))

if user_score >= 0 and user_score <=59:
  print("F")
elif user_score >= 60 and user_score <=69:
    print("D")
elif user_score >= 70 and user_score <=79:
    print("C")
elif user_score >= 80 and user_score <=89:
    print("B")
elif user_score >= 90 and user_score <=100:
    print("A")
