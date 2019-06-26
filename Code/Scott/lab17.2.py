"""
Name:           Scott Tran
Date            6/25/2019
Assignment:     Two words are anagrams of eachother if the letters of one can be rearranged to fit the other. e.g. anagram and nag a ram. Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not.

"""

def check_anagram(first, second):
    if first == second:
        print(True)
        print("The word you provided is an anagram!")
    else:
        print(False)
        print("Sorry, the word you provided is NOT an anagram.")
    
x = input("Give me a word to check if it's a anagram: "  )
x = x.lower().replace(" ", "")
x = sorted(x)

y = input("Give me a word to check if it's a anagram: "  )
y = y.lower().replace(" ", "")
y = sorted(y)

    



check_anagram(x,y)