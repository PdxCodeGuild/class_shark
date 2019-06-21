import string


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

    d_out = {}
    for item in d_in:
        count = 0
        t_val = 0
        for k in d_in:
            if k.startswith(item[0]):
                t_val += d_in[k]
                count += 1
        av = t_val / count
        d_out.setdefault(item[0], av)

    return d_out


d = {'a1':4, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}
print(unify(d))
