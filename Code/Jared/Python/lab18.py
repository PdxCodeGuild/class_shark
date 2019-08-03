# lab18 Peaks and Valleys

def peaks(heights):
    peaks_list = []
    for i in range(1, len(heights)-1):
        if heights[i-1] < heights[i] > heights[i+1]:
            peaks_list.append(i)
    return peaks_list  # this returns the index of the peaks


def valleys(heights):
    valleys_list = []
    for i in range(1, len(heights)-1):
        if heights[i-1] > heights[i] < heights[i+1]:
            valleys_list.append(i)
    return valleys_list  # returns index of the valleys


def peaks_valleys(heights):
    # p_v = peaks(heights) + valleys(heights)
    # p_v.sort()
    # return p_v
    return sorted(peaks(heights) + valleys(heights))

# def draw(heights):
#     p = peaks_valleys(heights)
#     while heights:
#     :





heights1 = [1, 3, 4, 2, 5, 3, 7, 6, 6, 5, 9, 4]
heights2 = [1, 2, 1, 2, 1, 4, 3, 3, 5, 6, 5, 8]

print(peaks(heights1))
print(valleys(heights1))
print(peaks_valleys(heights1))
print(peaks_valleys(heights2))

# print(draw(heights1)
