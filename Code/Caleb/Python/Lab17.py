# Lab 17: Palindrome & Anagram
# Palindrome: a palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a word that's equal to its own reverse.
# Write a function, 'check_palindrome', which takes a string, and returns True if the string's a palindrome, or False if it's not.
#   enter a word: racecar
#   'racecar' is a palindrome
#
#   enter a word: palindrome
#   'palindrome' is not a palindrome

print("Welcome to Lab 17. This program was coded in python by Caleb Mealey.")

def check_palindrome():
    print('This first function will test whether or not a user-inputted word is a palindrome.')
    input_word = str(input('Enter a word: '))
    len_of_input_word = int(len(input_word))
    input_word_reverse = ''
    for i in range(len_of_input_word):
        input_word_reverse += input_word[-i-1]
    print(input_word_reverse)
    if input_word == input_word_reverse:
        print(f'{input_word} is a palindrome')
    else:
        print(f'{input_word} is not a palindrome')
    


check_palindrome()


# Anagram:
# Two words are anagrams of eachother if the letters of one can be rearranged to fit the other. e.g. anagram and nag a ram.
# Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. The procedure for comparing the two strings is as follow:


def anagram():
    print('This second function will respond to the user whether or not two inputted words or phrases are anagrams of each other.')
    input_word1 = input('Enter the first word: ')
    input_word1_sort = input_word1.lower()
    input_word1_sort = input_word1_sort.replace(' ', '')
    input_word1_sort = sorted(input_word1_sort)
    input_word2 = input('Enter the second word: ')
    input_word2_sort = input_word2.lower()
    input_word2_sort = input_word2_sort.replace(' ', '')
    input_word2_sort = sorted(input_word2_sort)
    # print(input_word1_sort)
    # print(input_word2_sort)
    if input_word1_sort == input_word2_sort:
        print(f'\'{input_word1}\' and \'{input_word2}\' are anagrams')
    else:
        print(f'\'{input_word1}\' and \'{input_word2}\' are not anagrams')

anagram()