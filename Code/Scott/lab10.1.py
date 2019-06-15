"""
Name:           Scott Tran
Date            6/7/2019
Assignment:     Average a list of numbers.
"""

nums = [5, 0, 8, 3, 4, 1, 6]
total = 0

for i in nums:
    total += i
average = total/len(nums)
print(f"The average of the list {nums} is {round(average,1)}")
    