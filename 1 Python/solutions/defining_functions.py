# defining_functions.py
def hello(name='anon', age='unknown', location='unkown'):
    """
    prints greeting from three optional arguments
    """
    print(f"hello i'm {name}! i'm {age} years old and from {location}.")


def add(*args):
    """
    sums a variable number of arguments
    """
    # print(*args)
    total = 0
    for arg in args:
        total += arg
    return total


def print_kwargs(**kwargs):
    """
    prints keyword arguments
    """
    print(kwargs)
    for key in kwargs:
        print(key, kwargs[key])


def update(contact, **kwargs):
    """
    updates contact dictionary with keyword arguments
    """
    print(kwargs)
    contact.update(kwargs)


def find(l, target):
    """
    returns when target element is found in list l
    """
    for i in range(len(l)):
        if l[i] == target:
            print(f'found target at {i}')
            return
        print('not here...')


def same_length(a, b):
    """
    returns whether a and b are of the same length

    this example shows you that a return statement is like 'breaking' out 
    of a function. as soon as you hit one, you're out of the function
    """
    if len(a) == len(b):
        return 'same length'
    return 'different lengths'


def get_dimensions(w, h):
    """
    you can return multiple values
    python automatically packs them into a tuple
    """
    return w, h

width, height = get_dimensions(100, 200) # tuple unpacking
print(width)
print(height)
dimensions = get_dimensions(500, 500)
print(dimensions) # tuple

# name = input('name: ')
# age = input('age: ')
# location = input('location: ')
# h = hello(age, location, name)
# print(h)

# using keyword arguments you can have your arguments in any order
hello(location='pdx', name='bobert', age=12)
print('1+2=', add(1,2))
print('1+2+3=', add(1,2,3))
print(add())

print_kwargs(a='apples', b='beef')

contact = {'name': 'bobert', 'age': 12, 'location': 'unknown'}
print(contact)
update(contact, age=22, location='gotham', beard=True)
print(contact)

find(['orbs', 'borbs', 'gorbs'], 'lorbs')
find(['orbs', 'borbs', 'gorbs'], 'borbs')

print(same_length([1,2], [3,4,5]))