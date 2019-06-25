# lab0_knight.py
def knight(text):
    '''Return the string "knights who say Ni!"
    >>> print("Knights who say Ni!")
    Knights who say Ni!
    '''
    text = "Knights who say Ni!"
    return text


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(knight('text'))
