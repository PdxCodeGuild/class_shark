import random
'''
recursion requires
1: Base case            - in this case it is zero
2: recursive case       - in this case it is n + summation(n-1)
'''


def summation(n):
    '''
    returns the sum of n + n-1 + n-2 ...
    >>> summation(3)
    6

    >>> summation(4)
    10
    '''

    if n > 0:
        return n + summation(n-1)
    else:
        return n


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


# print(fib(30)) # fib(40) takes one minute

cached = [0, 1, 1, 2, 3, 5, 8, 13, 21]
def memoized_fib(n):
    if n < len(cached):
        return cached[n]
    else:
        comp = memoized_fib(n-1) + memoized_fib(n - 2)
        cached.append(comp)
        return comp

# print(memoized_fib(500))


def binary_search(l, target, start, end):
    mid = start + ((end - start) // 2)
    if end - start <= 0:
        return -1
    elif l[mid] == target:
        return mid
    elif l[mid] > target:
        return binary_search(l, target, mid+1, end)
    elif l[mid] < target:
        return binary_search(l, target, start, mid)


# lis = [i for i in range(50)]
# target = 23
# print(f'target was 23, target found =', binary_search(lis, target, 0, 50))

def merge_sort(l):
    if len(l) <= 1:
        return l
    elif len(l) == 2:
        if l[0] < l[1]:
            return l
        else:
            return [l[1], l[0]]

    mid = len(l)//2
    left = l[:mid]
    right = l[mid:]
    return merge(merge_sort(left), merge_sort(right))


def merge(l, r):
    i = 0
    j = 0
    merged = []
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            merged.append(l[i])
            i += 1
        else:
            merged.append(r[j])
            j += 1
    return merged + l[i:] + r[j:]


l = [random.choice(range(100)) for i in range(100)]
print(merge_sort(l))
print(merge_sort([18,19,6,8,32]))
