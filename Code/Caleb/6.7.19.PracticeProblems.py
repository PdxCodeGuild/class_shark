# practice.py

# Fundamentals 1
def is_even(a):
    return a % 2 == 0
   
   

# Fundamentals 2
def opposite(a, b):
#    opposite_check = False
#    if a/1 > 0:
#        a_positive = True
#    else:
#        a_positive = False
#    if b/1 > 0:
#        b_positive = True
#    else:
#        b_positive = False
#    if a_positive != b_positive:
#        opposite_check = True
#    return opposite_check

#    a_positive = a > 0
#    b_positive = b > 0
#    return a_positive != b_positive

    return (a > 0) != (b > 0)


# Tests
print(is_even(5)) # 
print(is_even(6)) # 

print(opposite(10,-1)) #
print(opposite(2, 3))
print(opposite(-1, -1)) #


# Problem 3
# Write a function that returns True if a number within 10 of 100.

def near_100(num):
    return 10 >= 100 - num >= -10
    
print(near_100(50)) # → False
print(near_100(99)) # → True
print(near_100(105)) # → True

# Problem 4
# Write a function that returns the maximum of 3 parameters.

def maximum_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return "All parameters are equal"


print(maximum_of_three(5,6,2)) # → 6
print(maximum_of_three(-4,3,10)) # → 10
print(maximum_of_three(1,1,1))

# Problem 5
# Print out the powers of 2 from 2^0 to 2^20

# 1, 2, 4, 8, 16, 32, ...

#base_list = [2]
# power_list = [0]
# final_list = []
# for i in range(1,21):
#    final_list.append(base_list.index(i)**power_list.index(i))
#    base_list.append(base_list.index(i)**power_list.index(i))
#    power_list.append(i+1)

# print(power_list)

def powered_list(x, y):
    squares = [x**2 for x in range(1, y)]
    return squares

print(powered_list(2, 20))