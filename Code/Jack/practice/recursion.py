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

print(memoized_fib(500))
