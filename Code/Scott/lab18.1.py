"""
Name:           Scott Tran
Date            6/19/2019
Assignment:     find 'peaks' and 'valleys' in a list of ints

a 'peak' is a number which is greater than the number on the left and right

a 'valley' is a number which is less that the number on the left and right
"""

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def peaks():
    peak = []
    for i in range(1, len(data)-1):
        left = data[i-1]
        middle = data[i]
        right = data[i+1]
        if left < middle and right < middle:
            peak.append(i)
    return peak   


def valleys():
    valley = []
    for i in range(1, len(data)-1):
        left = data[i-1]
        middle = data[i]
        right = data[i+1]
        if left > middle and right > middle:
            valley.append(i)
    return valley 

x = peaks()
y = valleys()
combined = sorted(list(set(x) | set(y)))

print(f"In the following list, {data}: ")
print(f"The peaks are at {x}.")
print(f"The valleys are at {y}.")
print(f"the combined positions for peaks and valleys is {combined}.")



