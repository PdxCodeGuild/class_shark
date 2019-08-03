# lab 17 anagram and palindrome

def check_palindrome(word):
    if str(word) == str(word)[::-1]:
        return True
    else:
        return False

user_word = input('Enter a word: ')

if check_palindrome(user_word) == True:
     print(f"{user_word} is a palindrome.")
else:
    print(f"{user_word} is not a palindrome.")


def anagram(word1, word2):
    if sorted(word1) == sorted(word2):
        return True


first_word = input('Enter a word: ').lower().replace(' ', '')
second_word = input('Enter a second word: ').lower().replace(" ", "")

if anagram(first_word, second_word) == True:
    print(f"{first_word} and {second_word} are anagrams.")
else:
    print(f"{first_word} and {second_word} are not anagrams.")



def anagram2(word1, word2):
    first_word = (word1).lower()
    first_word.replace(" ", "")
    #first_word = list(first_word)

    second_word = (word2).lower()
    second_word.replace(" ", "")
    #second_word = list(second_word)

    if sorted(first_word) == sorted(second_word):
        print(f"{first_word} and {second_word} is an anagram.")
    else:
        print(f"{first_word} and {second_word} is not an anagram.")

    return True

print(anagram2('vladimir nabokov', 'viviandark bloom'))
