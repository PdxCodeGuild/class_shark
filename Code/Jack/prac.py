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


ls1 = ['a', 'b', 'c', 'd', 'e']
ls2 = [1, 2, 3, 4, 5]
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
# print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis'))  # 2


def common_elements(nums1, nums2):
    # for num in nums1:
        # if num in nums2:
            # common.append(num)

    return [num for num in nums1 if num in nums2]

    # return [i for i in range(len(nums1)) if nums1[i] == nums2[i]]


ls1 = [1,2,3,4,5,6]
ls2 = [2,2,2,4,4,6]
print(ls1, ls2)
print(f'the common elements between ls1 and ls2 are {common_elements(ls1, ls2)}')
