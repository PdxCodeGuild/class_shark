"""
Name:           Scott Tran
Date            6/20/2019
Assignment:     Using the data list above, draw the image of X's above.
"""

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

a = [[1,2,1,2], [3,4,5,3], [8,9,4,3]]

# def printArray(arr):
#     for row in arr:
#         for item in row:
#             print("{:8.3f}".format(item), end = " ")
#         print("")

# printArray(a)

def mountain(x):
    for row in range(x):
        for i in range(row): 
            print("o"*x)

mountain(5)