# practice.py

# Fundamentals 1
def is_even(a):
    '''
    returns if a is even
    '''
    return a % 2 == 0
    # # equivalent to the line above
    # if a % 2 == 0:
    #     return True 
    # else:
    #     return False


# Fundamentals 2
def opposite(a, b):
    '''
    returns if a and b have opposite polarity
    '''
    # a_positive = a > 0
    # # # equivalent to the line above
    # # if a > 0:
    # #     a_positive = True 
    # # else:
    # #     a_positive = False

    # b_positive = b > 0
    # # # equivalent to the line above
    # # if b > 0:
    # #     b_positive = True 
    # # else:
    # #     b_positive = False

    # return a_positive != b_positive
    # # # equivalent to the line above    
    # # if a_positive != b_positive:
    # #     return True 
    # # else:
    # #     return False

    # one line solution equivalent to the lines above
    return (a > 0) != (b > 0)


# Strings 1
def double_letters(text):
    '''
    returns text with doubled letters
    '''
    # doubled = []
    # for letter in text:
    #     doubled.append(letter + letter)
    # return ''.join(doubled)

    # # equivalent to above
    return ''.join([letter + letter for letter in text])

    # doubled = ''
    # for letter in text:
    #     doubled += letter * 2
    # return doubled


# Strings 2
def missing_char(text):
    '''
    returns list of every permutation of text with a character missing
    '''
    missing = []
    for i in range(len(text)):
        left = text[:i]
        right = text[i+1:]
        # print(i, 'left', left, 'right', right)
        # # text[start:end:step] # slicing syntax
        missing.append(left + right)
    return missing


def powers_of_two(n):
    '''
    returns the n first powers of two
    '''
    return [2**i for i in range(n)]

    # # equivalent to above
    # nums = []
    # for i in range(n):
    #     nums.append(2**i)
    # return nums


def odds(n):
    '''
    returns odd numbers up to n
    '''
    return [i for i in range(n) if i % 2]

    # # equivalent to above
    # nums = []
    # for i in range(n):
    #     if i % 2 != 0:
    #         nums.append(i)
    # return nums




if __name__ == '__main__':
    # Tests
    print(is_even(5)) # → False
    print(is_even(6)) # → True

    print(opposite(10, -1)) # → True
    print(opposite(2, 3))  # → False
    print(opposite(-1, -1)) # → False

    print(double_letters('hello')) # -> 'hheelllloo'
    # print(double_letters(input('Enter a string you want to double: ')))
    print(missing_char('kitten')) # → ['itten', 'ktten', 'kiten', 'kiten', 'kittn', 'kitte']

    print(powers_of_two(10))
    print(odds(10))
