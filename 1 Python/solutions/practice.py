# practice.py

# Fundamentals 1
def is_even(a):
    '''
    returns if a is even
    '''
    return a % 2 == 0
    # # equivalent to the line above
    # if a % 2 == 0:
    #     return True 
    # else:
    #     return False


# Fundamentals 2
def opposite(a, b):
    '''
    returns if a and b have opposite polarity
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


# Tests
print(is_even(5)) # → False
print(is_even(6)) # → True

print(opposite(10, -1)) # → True
print(opposite(2, 3))  # → False
print(opposite(-1, -1)) # → False