fruits = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]


def combine(f, p):
    return dict(zip(f, p))


print(combine(fruits, prices))