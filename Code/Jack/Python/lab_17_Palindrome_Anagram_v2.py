def check_palindrome(s_in):
    count = 0
    for i in range(len(s_in)):
        if s_in[i] == s_in[(len(s_in)-1) - i]:
            count += 1
    if count == len(s_in):
        return True
    else:
        return False


def check_anagram(s_in1, s_in2):
    s_in1 = sorted(s_in1.lower().replace(' ', ''))
    s_in2 = sorted(s_in2.lower().replace(' ', ''))
    if s_in1 == s_in2:
        return True
    else:
        return False


TF = True
while TF:
    pal = input('Enter a word for Palindrome: ')
    pal = pal.lower().replace(' ', '')
    if check_palindrome(pal):
        print('\'' + pal + '\' is a palindrome')
    else:
        print('\'' + pal + '\' is not a palindrome')
    ana_one = input('Enter first word for anagram: ')
    ana_two = input('Enter second word: ')
    if check_anagram(ana_one, ana_two):
        print('\'' + ana_one + '\' and',
              '\'' + ana_two + '\' are anagrams')
    else:
        print('\'' + ana_one + '\' and',
              '\'' + ana_two + '\' are not anagrams')
    chc = input('again?')
    if chc.startswith('n'):
        TF = False
