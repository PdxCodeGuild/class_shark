import string
from random import randint
from runtime import get_runtime as gt_r

def comb(ls1, ls2):
    # d_tmp = {}
    # for i in range(len(ls1)):
    #     d_tmp[ls1[i]] = ls2[i]
    # return d_tmp

    # Comprehension 1
    # return {ls1[i]: ls2[i] for i in range(len(ls1))}

    # Comprehension 2
    return {dict(zip(ls1, ls2))}


# ls1 = ['a', 'b', 'c', 'd', 'e']
# ls2 = [1, 2, 3, 4, 5]
# print(comb(ls1, ls2))


def latest_letter(usr_wrd):
    last = ''
    alpha = string.ascii_letters
    for letter in usr_wrd:
        if alpha.find(letter) > alpha.find(last):
            last = letter
    return last


# letter = latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')
# print('the last letter is:', letter)
# print(latest_letter('123'))

def cat_dog(wrd):
    cat_count = 0
    dog_count = 0
    for i in range(len(wrd)):
        if wrd[i:i+3] == 'cat':
            cat_count += 1
        elif wrd[i:i+3] == 'dog':
            dog_count += 1
    return cat_count == dog_count


# print('catdog'*5, cat_dog('catdog'*5))
# print('catcatdog', cat_dog('catcatdog'))


def count_letter(letter, word):
    count = 0
    for item in word:
        if item == letter:
            count += 1
    return count


# print(count_letter('i', 'antidisestablishmentterianism'))  # 5
# print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis'))  #2


def common_elements(nums1, nums2):

    # set1 = set(nums1)
    # set2 = set(nums2)

    # return [num for num in set(nums1) if num in set(nums2)]
    return list(set(nums1) & set(nums2))

    # a & b AND
    # a | b OR
    # a - b Diff
    # a ^ b XOR


# ls1 = [1,2,3,4,5,6]
# ls2 = [2,2,2,4,4,6]
# print(ls1, ls2)
# print(f'the common elements between ls1 and ls2 are {common_elements(ls2, ls1)}')


# dict prac prob 1
def combine(ls1, ls2):
    # t_dict = {}
    # for i in range(len(ls1)):
    #     t_dict[ls1[i]] = ls2[i]
    #
    # return t_dict

    return {ls1[i]: ls2[i] for i in range(len(ls1))}


# fruits = ['apple', 'banana', 'pear']
# prices = [1.2, 3.3, 2.1]
# dict = combine(fruits, prices)
# print(dict.items())


# dict prac prob 2
def average(d_in):
    # f_avg = 0.0
    # for f_val in d_in.values():
    #     f_avg += f_val
    # f_avg /= len(d_in.values())
    #
    # return f_avg

    return float('{0:.2f}'.format(sum(d.values()) / len(d)))


# print(average(dict))


def unify(d_in):

    # d_out = {}
    # for item in d_in:
    #     count = 0
    #     t_val = 0
    #     for k in d_in:
    #         if k.startswith(item[0]):
    #             t_val += d_in[k]
    #             count += 1
    #     av = t_val / count
    #     d_out.setdefault(item[0], av)
    #
    # return d_out

    d_out = {}
    count = {}
    for key, val in d_in.items():
        d_out[key[0]] = d_out.get(key[0], 0) + val
        count[key[0]] = count.get(key[0], 0) + 1

    # for k, v in d_out.items():
    #     d_out[key] = val / count[key]
    # return d_out

    return {key: val / count[key] for key, val in d_out.items()}


# d = {'a1':4, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}
# print(unify(d))

@gt_r
def find_pair(num, target):
    # for i in range(len(num)):
    #     for j in range(i+1, len(num)):
    #         if num[i] + num[j] == target:
    #             return [i, j]

    # for s1 in num:
    #     s1_ind = num.index(s1)
    #     match = target - s1
    #     if match in num and num.index(match) != s1_ind:
    #         print(s1, s1_ind)
    #         return [s1_ind, num.index(match)]

    num_set = set(num)
    for n in num_set:
        if target - n in num_set and num.index(n) != num.index(target - n):
            return [num.index(n), num.index(target - n)]


# nums = [randint(0, 250) for i in range(1000)]
# target = 11
# sum1, sum2 = find_pair(nums, target)
# print(nums[sum1], '+', nums[sum2], '=', target)


def combine_all(l_nest):
    '''
    takes in nested list and unpacks it into a single list

    >>> combine_all([[5, 2, 3], [4, 5, 1], [7, 6, 3]])
    [5, 2, 3, 4, 5, 1, 7, 6, 3]

    '''
    # # writen out form of comprehension below
    # t_l_out = []
    # for layer1 in l_nest:
    #     for layer2 in layer1:
    #         t_l_out.append(layer2)
    #
    # return t_l_out

    # # comprehension
    # return [j for layer1 in l_nest for j in layer1]


###############################################################################
    # # this version will take in any number of nests within a list
    temp = []
    for layer1 in l_nest:
        if type(layer1) == type(l_nest):
            temp += combine_all(layer1)
        else:
            temp.append(layer1)
    return temp


# num = [[[5, 2, 3], [4, 5, 1], [7, 6, 3]], [[5, 2, 3], [4, 5, 1], [7, 6, 3]], [[5, 2, 3], [4, 5, 1], [7, 6, 3]]]
# num = [[5, 2, 3], [4, 5, 1], [7, 6, 3]]
# num = [[[[1,2], [3,4], [5,6]], [[1,2], [3,4], [5,6]], [[1,2], [3,4], [5,6]], [1,2], [3,4], [5,6]], [[[1,2], [3,4], [5,6]], [[1,2], [3,4], [5,6]], [[1,2], [3,4], [5,6]], [1,2], [3,4], [5,6]]]
# print(combine_all(num))

def outer():
    x = 'here'

    def inner():
        x = 'inner'
        print(x)

    def inner2():
        nonlocal x
        print(x)

    if x != 'here':
        return inner
    else:
        return inner2


def multiply(x):
    def times(y):
        return x * y
    return times


times_three = multiply(3)
times_four = multiply(4)

# outer()()
# it = outer()
# it()
# print(times_three(10))
# print(times_four(10))


def minimum(nums):
    '''
    >>> minimum([1, 2, 3, -9000, 0])
    -9000
    '''
    return min(nums)


def maximum(nums):
    '''
    >>> maximum([1, 2, 3, 9000, 0])
    9000
    '''
    return max(nums)


def mean(nums):
    '''
    >>> mean([1,2,3,4,5,6,6,6,5,4,3])
    6
    '''
    return sum(nums)/len(nums)


def mode(nums):
    d = {}
    for num in nums:
        d[num] = d.get(num, 0) + 1
    mode = max(d.values())
    for k, v in d.items():
        if v == mode:
            return k
    return None
