# recursion.py
import time

def get_runtime(fn):
    '''
    decorator to print runtime of function
    '''
    start = time.time()

    def invoke(*args, **kwargs):
        ret = fn(*args, **kwargs)
        print(f'{fn.__name__} completed in {time.time() - start} s.')
        return ret

    return invoke


def memoize(fn):
    '''
    decorator to memoize functions
    '''
    cache = []

    def invoke(n):
        if n < len(cache): # base case
            # if we've computed fn(n) before, grab it from cache
            return cache[n]
        else: # recursive case
            ret = fn(n) # compute new n
            cache.append(ret) # add to cache
            return ret

    return invoke


def summation(n):
    '''
    returns the sum of n + n-1 + n-2 + ... + 0

    >>> summation(3) # 3 + 2 + 1
    6
    >>> summation(4) # 4 + 3 + 2 + 1
    10
    '''
    if n <= 1: # base case
        return n
    total =  n + summation(n-1) # recursive case

    return total


def countdown(n):
    '''
    prints countdown fron n to 0
    '''
    print(n)
    if n == 0: # base case
        return
    countdown(n-1) # recursive case


def countup(n):
    '''
    prints countdown fron 1 to n
    '''    
    if n == 0: # base case
        return
    countup(n-1) # recursive case
    print(n)


# @get_runtime
@memoize
def fib(n):
    '''
    returns nth fibonacci number
    '''
    if n == 0 or n == 1: # base cases
        return n 
    return fib(n-1) + fib(n-2) # recursive case

# @get_runtime
def fib_loop(n):
    '''
    returns nth fibonacci number without recursion
    '''
    fibs = [0, 1] # base cases

    for i in range(2, n+1):
        # compute ith fibonacci number as sum of fib(i-1) + fib(i-2)
        # until we reach n
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs[n]


cache = [0, 1] # base cases
# @get_runtime
def memoized_fib(n):
    '''
    returns nth fibonacci number
    uses memoization (storing computed values) to optimize performance
    '''
    if n < len(cache): # base case
        return cache[n] # we've computed n before, so get it from cache

    # else compute new fibonacci number recursively
    new_fib = memoized_fib(n-1) + memoized_fib(n-2)
    cache.append(new_fib) # add it to cache
    return new_fib


def factorial(n):
    '''
    returns n!

    >>> factorial(5) # 5 x 4 x 3 x 2 x 1
    120
    >>> factorial(4)
    24
    '''
    print(n)
    if n == 1:
        return 1
    return n * factorial(n-1)


def binary_search(l, target, start, end):
    '''
    :l: sorted list
    :start: index
    :end: index

    returns index of target in list l, or -1 if target doesn't exist
    '''
    mid = start + ((end - start) // 2) # grab midpoint index between start and end
    # print('search area:', l[start:end], f'mid: l[{mid}]', l[mid], 'target:', target)
    if end - start <= 0: # base case: empty search area, target not found
        return -1
    if l[mid] == target: # base case: target found at mid
        return mid
    elif l[mid] < target: # search right half
        return binary_search(l, target, mid+1, end)
    elif l[mid] > target: # search left half
        return binary_search(l, target, start, mid)


def merge(l1, l2):
    '''
    merges two sorted lists 

    l1 = [3,5,7]
    l2 = [1,6]
    '''
    i = 0
    j = 0
    merged = []
    # print('l1', l1, 'l2', l2)
    while i < len(l1) and j < len(l2):
        # print('i', i, 'j', j, 'merged', merged)
        if l1[i] < l2[j]:
            merged.append(l1[i])
            i += 1 
        else:
            merged.append(l2[j])
            j += 1

    # print('merged', merged +  l1[i:] + l2[j:])
    return merged + l1[i:] + l2[j:]


def merge_sort(l):
    '''
    :l: list
    returns sorted list

    Mergesort is a divide and conquer algorithm. We divide the list in half until 
    we have pieces that are so small they become trivial to sort. Then, we merge
    the sorted sublists together until we end up with a sorted list.
    '''
    print(l)
    if len(l) <= 1: # base cases: an empty list or a list of one is already sorted
        return l
    elif len(l) == 2: # base case: in a list of 2, the smaller one is first, the larger second
        if l[0] < l[1]:
            return l
        else:
            return [l[1], l[0]]


    mid = len(l) // 2
    left = l[:mid]
    right = l[mid:]
    print('left', left, 'right', right)
    # we then recursively sort each half of the list and merge them together
    return merge(merge_sort(left), merge_sort(right)) # recursive case


if __name__ == '__main__':

    # print(summation(4))
    # print(countdown(10))
    # print(countup(10))
    # n = 10

    # j
    # while (n > 0):
    #     print(n)
    #     n -= 1

    # for i in range(1000000):
    #     try:
    #         memoized_fib(i)
    #     except Exception as e:
    #         print(getattr(e, 'message', repr(e)))
    #         print(getattr(e, 'message', str(e)))
    #         print('breaks at fib', i)
    #         break

    # start = time.clock()
    # n = 2000
    # for i in range(2, n, 20):
    #     fib(i)
    #     memoized_fib(i)
    #     fib_loop(i)

    # print(fib(n))
    # print(fib.__name__, 'completed in', time.clock() - start)
    # start = time.clock()
    # print(memoized_fib(n))
    # print(memoized_fib.__name__, 'completed in', time.clock() - start)
    # start = time.clock()
    # print(fib_loop(n))
    # print(fib_loop.__name__, 'completed in', time.clock() - start)

    # # print(factorial(3))
    l = [0,4,5,7,8,10,16]
    # print(binary_search(l, 4, 0, len(l)))
    # print(binary_search(l, 16, 0, len(l)))
    print(binary_search(l, 14, 0, len(l)))
    print(merge_sort([18,19,6,8,32,1000,-2,35,1,1,1,1]))