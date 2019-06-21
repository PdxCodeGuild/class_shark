# Lab 18: Peaks & Valleys
# define the following functions:
# 1. peaks - returns the indices of peaks. A peak has a lower number on both the left and the right.
# 2. valleys - returnts the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
# 3. peaks_and_valleys - uses the above two functions to compile a single list of the peaks and vallyes in order of appearance in the original data.

# Declare the data set provided by the instructor as a list of integers
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# Define a function 'peaks', with one parameter 'a', return a list of the peaks from the inputted data set
def peaks(a):
    peaks_list = []
    # Crucial to pay attention to how range is used, see how it begins at index 1 but ends at one index for the final item in the inputted list
    for i in range(1,len(a)-1): 
        # print(f'preceding value = {a[i-1]}') ## Used for testing code
        # print(f'current value = {a[i]}')
        # print(f'next value = {a[i+1]}')
        # print(f'current index = {i}')
        if a[i-1] < a[i] and a[i+1] < a[i]:
            peaks_list.append(i)
        # print('-'*60)
    return peaks_list


# print(peaks(data))

# Define a function 'valleys', with one parameter 'b', return a list of the valleys from the inputted data set
def valleys(b):
    valleys_list = []
    for h in range(1,len(b)-1):
        if b[h-1] > b[h] and b[h+1] > b[h]:
            valleys_list.append(h)
    return valleys_list


# print(valleys(data))


# Define a function 'peaks_and_valleys', with two parameters, 'c' & 'd', return a list of concantenated & sorted peaks and valley lists
def peaks_and_valleys(c, d):
    peaks_and_valleys_list = c + d
    peaks_and_valleys_list.sort()
    return peaks_and_valleys_list


# print(peaks_and_valleys(peaks(data), valleys(data)))

# Version 2: Using the data list above, draw the image of x's above

def visual():
    row1 = ''
    row2 = ''
    row3 = ''
    row4 = ''
    row5 = ''
    row6 = ''
    row7 = ''
    row8 = ''
    row9 = ''
    for i in data:
        if i == 9:
            row1 += ' x '
        else:
            row1 += '   '
        if i == 8:
            row2 += ' x '
        elif i > 8:
            row2 += ' x '
        else:
            row2 += '   '
        if i == 7:
            row3 += ' x '
        elif i > 7:
            row3 += ' x '
        else:
            row3 += '   '
        if i == 6:
            row4 += ' x '
        elif i > 6:
            row4 += ' x '
        else:
            row4 += '   '
        if i == 5:
            row5 += ' x '
        elif i > 5:
            row5 += ' x '
        else:
            row5 += '   '
        if i == 4:
            row6 += ' x '
        elif i > 4:
            row6 += ' x '
        else:
            row6 += '   '
        if i == 3:
            row7 += ' x '
        elif i > 3:
            row7 += ' x '
        else:
            row7 += '   '
        if i == 2:
            row8 += ' x '
        elif i > 2:
            row8 += ' x '
        else:
            row8 += '   '
        if i == 1:
            row9 += ' x '
        elif i > 1: 
            row9 += ' x '
        else:
            row9 += '   '
    print(row1)
    print(row2)
    print(row3)
    print(row4)
    print(row5)
    print(row6)
    print(row7)
    print(row8)
    print(row9)
    print(data)


visual()
print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(peaks(data), valleys(data)))
