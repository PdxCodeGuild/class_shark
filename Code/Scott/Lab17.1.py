"""
Name:           Scott Tran
Date            6/24/2019
Assignment:     A palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a word that's equal to its own reverse. Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.

"""

def palindrome():

    x = input("Give me a word to check if it's a palindrome: "  )
    if x == x[::-1]:
        print(True)
        print("The word you provided is a palindrome!")
    else:
        print(False)
        print("Sorry, the word you provided is NOT a palindrome.")

palindrome()
    