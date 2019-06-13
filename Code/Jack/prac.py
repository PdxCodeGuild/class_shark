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
print(comb(ls1, ls2))
