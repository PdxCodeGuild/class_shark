# Lab 10: Average Numbers

# Version 1:
# We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list. Remember, 'len' will give you the length of a list.

def Version_1(list_of_nums):
    total = 0
    for num in list_of_nums:
        total += num
    sum = total / len(list_of_nums)
    return sum


print(Version_1([5, 0, 8, 3, 4, 1, 6]))

# Version 2:
# Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average. The following code demonstrates how to add an element to the end of a lsit.


def Version_2():
    TF = True
    version_2_list = []
    list_add_x = input('Enter a number, or \'done\': ')
    while TF:
        if list_add_x == 'done':
            TF = False
        else:
            version_2_list.append(int(list_add_x))
            list_add_x = input('Enter a number, or \'done\': ')
    mean = sum(version_2_list) / len(version_2_list)
    return mean


print(Version_2())
