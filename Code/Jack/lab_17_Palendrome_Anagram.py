import string
#import re


# def regEx(s):
#     pattern = re.compile(r'([A-Z]+)([a-z]+)'')
#
#     for letters, number) in re.findall(pattern, s):
#         print(numbers, '*', letters)


def ana_One():

    i = 0
    k = 1
    d_Words = []

    ana = input('Please enter your first word:')
    ana = scrub_Input_Punc(ana)
    d_Words.append(build_Dict(ana))
    TF = True
    while TF:
        ana = input('Please enter your next word:')
        ana = scrub_Input_Punc(ana)
        d_Words.append(build_Dict(ana))
        TF = ask()
    not_Ana_Count = 0
    for dict in d_Words:
        for dict2 in d_Words:
            if dict != dict2:
                not_Ana_Count += 1
    if not_Ana_Count > 0:
        print('Some of your words are not anagrams.')
    else:
        print('All of your words ARE anagrams!')


def ask():
    choice = input('Would you like to enter another word? y/n ')
    if choice == 'y':
        return True
    else:
        return False


def build_Dict(ana_In):
    d_Letter_Count = {}
    for letter in ana_In:
        d_Letter_Count[letter] = 0
    for letter in ana_In:
        if letter in string.ascii_letters:
            d_Letter_Count[letter] = d_Letter_Count[letter] + 1
    return d_Letter_Count


def scrub_Input_Punc(ana_In_String):
    for char in ana_In_String:
        if char in string.punctuation:
            ana_In_String = ana_In_String.replace(char, '')
    return ana_In_String


def again():
    choice = input('would you like to go again? y/n\n')
    if choice == 'y':
        return True
    elif choice == 'n':
        print('\nGoodBye!\n')
        return False
    else:
        print('\nincorrect input:\n')
        return True


TF = True
print('Welcome to the Anagram Checker!')
while TF:
    ana_One()
    TF = again()
