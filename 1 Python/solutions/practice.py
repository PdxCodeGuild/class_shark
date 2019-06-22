'''
practice.py

practice python problems
'''

from time import clock
from string import (ascii_letters as alpha, punctuation)


def get_runtime(fn):
    def timer(*args, **kwargs):        
        start = clock()
        result = fn(*args, **kwargs)
        print(f'Completed {fn.__name__} in {clock() - start} s')
        return result
    
    return timer 


# Fundamentals 1
def is_even(a):
    '''
    :a: int

    returns if a is even
    >>> is_even(5)
    False
    >>> is_even(6)
    True
    '''
    return a % 2 == 0
    # # equivalent to the line above
    # if a % 2 == 0:ppython
    #     return True 
    # else:
    #     return False
    # 

# Fundamentals 2
def opposite(a, b):
    '''
    :a: int
    :b: int

    returns if a and b have opposite polarity

    >>> opposite(10, -1)
    True
    >>> opposite(2, 3)
    False
    >>> opposite(-1, -1)
    False
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

    >>> double_letters('hello')
    'hheelllloo'
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

    >>> missing_char('kitten')
    ['itten', 'ktten', 'kiten', 'kiten', 'kittn', 'kitte']
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

    >>> odds(10)
    [1, 3, 5, 7, 9]
    '''
    return [i for i in range(n) if i % 2]

    # # equivalent to above
    # nums = []
    # for i in range(n):
    #     if i % 2 != 0:
    #         nums.append(i)
    # return nums


# Lists 3 
@get_runtime
def eveneven(nums):
    '''
    :nums: list

    returns true if there is an even number of evens in nums

    >>> eveneven([5, 5, 2])
    False    
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

    >>> eveneven_comprehension([5, 5, 2])
    False
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
    >>> latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')
    'v'
    >>> latest_letter('123')
    ''
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

    >>> count_hi('hihi')
    2
    >>> count_hi('wallaby')
    0
    >>> count_hi('')
    0
    '''
    count = 0
    for i in range(len(text)-1):
        # if text[i:i+2] == 'hi':
        #     print(i, text[i])
        if text[i] + text[i+1] == 'hi':
            count += 1
    return count


# Lists 7
@get_runtime
def common_elements(list1, list2):
    '''
    returns list of common elements between list1 and list2

    >>> count_hi('high noon in ohio')
    2
    >>> common_elements([1,2,3], [2,3,4,5])
    [2, 3]
    >>> common_elements([1,2,2,3,3,3,3], [2,3,3,4,5])
    [2, 3]
    >>> common_elements([1,2,3], [4,5,6])
    []  
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

    >>> common_set_elements([1,2,3], [2,3,4,5])
    [2, 3]
    >>> common_set_elements([1,2,2,3,3,3,3], [2,3,3,4,5])
    [2, 3]
    >>> common_set_elements([1,2,3], [4,5,6])
    []    
    '''
    set1 = set(list1)
    set2 = set(list2)

    return list(set1 & set2)


# Dict 2
def average(d):
    '''
    :d: dict
    returns the average of d's values

    >>> average({'apple':1.2, 'banana':3.3, 'pear':2.1}) == 2.2
    True
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

    >>> powers_of_two(10) == [1, 2, 4, 8, 16, 32, 64, 128, 256,512]  
    True
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

    evens(10)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18. 20]
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


# Dict 3
def average_values(d):
    '''
    :d: dict
    returns dict of average values for keys that start with the same letter

    >>> average_values({'a1':4, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}) == {'a':3.0, 'b':4.0, 'c':5.0}
    True
    >>> average_values({'apples': 2, 'beef': 0.99, 'cherries': 7, 'crawfish': 5}) == {'a':2.0, 'b':.99, 'c':6.0}
    True
    '''
    sums = {}
    count = {}

    for key, val in d.items():
        # print(key, key[0])
        # if key[0] in sums:
        #     sums[key[0]] += val
        # else:
        #     sums[key[0]] = val
        # # equivalent to above
        sums[key[0]] = sums.get(key[0], 0) + val
        count[key[0]] = count.get(key[0], 0) + 1

    # avgs = {}
    # for key, val in sums.items():
    #     avgs[key] = val / count[key]
    # return avgs

    # # equivalent to above for loop
    return {key: val / count[key] for key, val in sums.items()}


def find_pair(nums, target):
    '''
    :nums: list of numbers
    :target: number

    returns pair of numbers from :nums: that sum to a target number
    '''
    pass 


# @get_runtime
def brute_force_find_pair(nums, target):
    '''
    >>> brute_force_find_pair([5, 6, 2, 3], 7)
    [5, 2]
    '''
    count = 0
    for i in nums:
        for j in nums:
            count += 1
            x = i + j 
            if target == x:
                return [i, j]
    print(count, 'tries')


# @get_runtime
def optimized_brute_force_find_pair(nums, target):
    '''
    >>> optimized_brute_force_find_pair([5, 6, 2, 3], 7) 
    [5, 2]
    '''
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            count += 1
            x, y = nums[i], nums[j] 
            if target == x + y:
                return [x, y]
    print(count, 'tries')


@get_runtime
def optimized_sort_find_pair(nums, target):
    '''
    >>> sorted(optimized_sort_find_pair([5, 6, 2, 3], 7)) == [2,5]
    True
    '''    
    nums.sort()
    count = 0
    for i in range(len(nums)):
        for j in range(len(nums)-1, i, -1):
            x, y = nums[i], nums[j]
            count += 1            
            if target == x + y:
                return [x, y]
            elif target > x + y:
                break
    print(count, 'tries')


@get_runtime
def haha_found_pair(nums, target):
    '''
    >>> haha_found_pair([5, 6, 2, 3], 7)
    [5, 2]
    '''    
    count = 0
    num_set = set(nums)
    for i in range(len(nums)):
        x = nums[i]
        count += 1                    
        match = target - x 
        print(i, x, match)
        if match in num_set:
            return [x, match]
    print(count, 'tries')


@get_runtime
def not_optimized_optimized_haha_found_pair(nums, target):
    '''
    >>> sorted(not_optimized_optimized_haha_found_pair([5, 6, 2, 3], 7)) == [2, 5]
    True
    '''    
    count = 0
    seen = {}
    for i in range(len(nums)):
        x = nums[i]
        count += 1                    
        match = target - x 
        print(i, x, match)
        if seen.get(match) == x:
            return [x, match]
        seen[x] = match
    print(count, 'tries')
    

@get_runtime
def optimized_set_find_pair(nums, target):
    num_set = set(nums)
    # diff_set = {target - x for x in nums}
    for num in num_set:
        if target - num in num_set:
            return [num, target-num]
    # return [[num, target - num] for num in num_set & diff_set]


if __name__ == '__main__':
    pass

