# practice.py
from time import clock
from string import (ascii_letters as alpha, punctuation)

# Fundamentals 1
def is_even(a):
    '''
    :a: int

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
    :a: int
    :b: int

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
    :text: string
    
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
    :text: string

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


def odds(n):
    '''
    :n: int

    returns odd numbers up to n
    '''
    return [i for i in range(n) if i % 2]

    # # equivalent to above
    # nums = []
    # for i in range(n):
    #     if i % 2 != 0:
    #         nums.append(i)
    # return nums


def get_runtime(fn):
    def timer(*args, **kwargs):        
        start = clock()
        result = fn(*args, **kwargs)
        print(f'Completed {fn.__name__} in {clock() - start} s')
        return result
    
    return timer


# Lists 3 
@get_runtime
def eveneven(nums):
    '''
    :nums: list

    returns true if there is an even number of evens in nums
    '''
    # evens = 0
    # for item in nums:
    #     if item % 2 == 0:
    #         evens += 1
    # return evens % 2 == 0
    evens = []
    for i in nums:
        if int(i) % 2 == 0:
            evens.append(i)

    return len(evens) % 2 == 0

@get_runtime
def eveneven_comprehension(nums):
    '''
    equivalent to the solution above
    '''
    return len([i for i in nums if int(i) % 2 == 0]) % 2 == 0


# Dict 1
def combine(keys, values):
    '''
    :keys: list
    :values: list

    returns dictionary of keys and values 
    '''
    combined = {}
    for i in range(len(values)):
        combined[keys[i]] = values[i]
    return combined

    # equivalent comprehension to solution above
    return {keys[i]: values[i] for i in range(len(keys))}

    # alternate comprehension solution
    return {key: value for key, value in zip(keys, values)}

    # best solution
    return dict(zip(keys, values))


def latest_letter(text):
    '''
    :text: string
    returns the letter that appears the latest in the english alphabet
    '''
    translator = str.maketrans('', '', punctuation + '1234567890')
    text = text.translate(translator).lower() # remove punctuation and make lowercase

    last = ''
    for letter in text:
        if alpha.find(letter) > alpha.find(last):
            last = letter 
    return last

    return max(text)


def count_hi(text):
    '''
    :text: string
    returns the number of occurances of 'hi' in a given string
    '''
    count = 0
    for i in range(len(text)-1):
        # if text[i:i+2] == 'hi':
        # print(i, text[i])
        if text[i] + text[i+1] == 'hi':
            count += 1
    return count


# Lists 7
@get_runtime
def common_elements(list1, list2):
    '''
    returns list of common elements between list1 and list2
    '''
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

    return [item for item in list1 if item in list2]


@get_runtime
def common_set_elements(list1, list2):
    '''
    set implementation of common_elements()
    '''
    set1 = set(list1)
    set2 = set(list2)

    return list(set1 & set2)


# Dict 2
def average(d):
    '''
    :d: dict
    returns the average of d's values
    '''
    # count = 0
    # total = 0
    # for key in d:
    #     count += 1 
    #     total += d[key]
    # return float("{0:.2f}".format(total / count))

    return float('{0:.2f}'.format(sum(d.values()) / len(d)))


# Comprehensions 1
def powers_of_two(n):
    '''
    :n: int

    returns the n first powers of two
    '''
    return [2**i for i in range(n)]
    
    # # equivalent to above
    # nums = []
    # for i in range(n):
    #     nums.append(2**i)
    # return nums

    # # bitwise left shift operator
    # return [1 << exp for exp in range(n)]


# Comprehensions 2
@get_runtime
def evens(n):
    '''
    :n: int
    returns the first n even numbers
    '''
    return [2*i for i in range(n)] # map
    # # equivalent to above
    # evens_list = []
    # for i in range(n):
    #     evens_list.append(2*i)    
    # return evens_list

    return [i for i in range(n*2) if i % 2 == 0] # filter
    # # equivalent to above
    # evens_list = []
    # for i in range(n*2):
    #     if i % 2 == 0:
    #         evens_list.append(i)
    # return evens_list



@get_runtime
def evens_range(n):
    return list(range(0,20,2))


if __name__ == '__main__':
    # # Tests
    # print(is_even(5)) # → False
    # print(is_even(6)) # → True

    # print(opposite(10, -1)) # → True
    # print(opposite(2, 3))  # → False
    # print(opposite(-1, -1)) # → False

    # print(double_letters('hello')) # -> 'hheelllloo'
    # print(missing_char('kitten')) # → ['itten', 'ktten', 'kiten', 'kiten', 'kittn', 'kitte']

    # print(powers_of_two(10)) # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    # print(odds(10)) # [1, 3, 5, 7, 9]

    # start = clock()
    # print(eveneven([5, 5, 2])) # → False
    # print('loop done in: ',  clock() - start,  's')
    # start = clock()
    # print(eveneven_comprehension([5, 5, 2])) # → False

    # print(get_runtime(eveneven([2,3,4])))
    # print('comprehension done in: ', clock() - start , 's')
    # k = ['a', 'b', 'c']
    # v = ['apples', 'beef', 'corn']
    # print(combine(k, v))
    # print(latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')) # -> 'v'
    # print(latest_letter('123')) # -> 'v'
    # print(count_hi('hihi')) # -> 2 
    # print(count_hi('wallaby')) # -> 0 
    # print(count_hi('')) # -> 0 
    # print(count_hi('high noon in ohio')) # -> 2
    # print(common_elements([1,2,3], [2,3,4,5])) # [2, 3]
    # print(common_elements([1,2,2,3,3,3,3], [2,3,3,4,5])) # [2, 3]
    # print(common_elements([1,2,3], [4,5,6])) # []

    # print(common_set_elements([1,2,3], [2,3,4,5])) # [2, 3]
    # print(common_set_elements([1,2,2,3,3,3,3], [2,3,3,4,5])) # [2, 3]
    # print(common_set_elements([1,2,3], [4,5,6])) # []

    
    # combined = {'apple':1.2, 'banana':3.3, 'pear':2.1}
    # print(average(combined)) # -> 2.2

    print(powers_of_two(10))
    print(evens(10))
    print(evens_range(10))
