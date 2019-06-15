# rot13.py
from string import (ascii_lowercase as lower, ascii_uppercase as upper)

def encode(text, rotation=13):
    '''
    :text: string
    :rotation: int
    return text rotated by rotation
    '''
    cyph = []

    for letter in text:
        if letter.islower():
            cyph.append(lower[(lower.find(letter) + rotation) % 26])
        elif letter.isupper():
            cyph.append(upper[(upper.find(letter) + rotation) % 26])
        else:
            cyph.append(letter)    
    return ''.join(cyph)


def encode_dict_solution(text, rotation=13):
    '''
    dict implementation
    '''
    rotation %= 26
    # rotation = rotation % 26
    translate = dict(zip(lower, lower[rotation:] + lower[:rotation]))
    translate.update(dict(zip(upper, upper[rotation:] + upper[:rotation])))
    cyph = ''
    for letter in text:
        cyph += translate.get(letter, letter)
        # if letter in translate:
        #     cyph += translate[letter]
        # else:
        #     cyph += letter
    return cyph


def encode_ascii_solution(text, rotation=13):
    '''
    ascii implementation
    '''
    upper = range(65, 91) # upper 65-90
    lower = range(97, 123) # lower 97-122
    cyph = ''
    for letter in text:
        ascii_val = ord(letter)
        if letter.isalpha():
            if ascii_val in upper:
                shift = 65
            elif ascii_val in lower:
                shift = 97
            ascii_val -= shift
            rotated = (ascii_val + rotation) % 26            
            cyph += chr(rotated + shift)
        else:
            cyph += letter
    return cyph


def decode(text, rotation=13):
    '''
    :text: string
    :rotation: int
    return text rotated by -rotation
    '''
    return encode(text, -rotation)


def main():
    # # tests
    # message = 'hello with spaces'
    # coded = encode(message, 100)
    # decoded = decode(coded, 100)
    # print(message, coded, decoded)

    # print(encode_dict_solution(message, 100))
    # print(encode_ascii_solution(message, 100))

    print('-'*60)
    print('Welcome to the ROT-Cypher')
    print('-'*60)

    play_again = True

    while play_again:
        msg = input('Enter as message: ')

        invalid = True
        while invalid:
            cypher = input('(e)ncode or (d)ecode: ').strip().lower()
            if cypher in ['encode', 'e', 'decode', 'd']:
                invalid = False

        tries = 0
        invalid = True
        while invalid:
            try:
                rot = int(input('How much to rotate by: '))
                invalid = False
            except ValueError:
                tries += 1
                if tries < 3:
                    print('Enter a number')
                else:
                    print('ur dumb :,(((')

        if cypher.startswith('e'):
            print('Encrypting...')
            print(encode(msg, rot))
        else:
            print('Decrypting...')
            print(decode(msg, rot))

        while True:
            again = input('Do you want to play again: ').strip().lower()
            if again in ['yes', 'y', 'no', 'n']:
                play_again = again.startswith('y')
                break


main()