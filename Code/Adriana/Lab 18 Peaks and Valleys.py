#Lab 18 Peaks and Valleys

#peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

#valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

#peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

def peaks(data):
    peak_location = []
    #returns location peaks
    #a peaks has a lower number on BOTH SIDES
    for i in range(1, len(data)-1):
        left_side = data[i-1]
        right_side = data[i+1]
        mid = data[i]
        if left_side < mid and right_side <  mid:
            peak_location.append(i)
    return peak_location

    #print (peak_location)
    #print(peak_location[i-1:i+2], peak_location[i-1]+peak_location[i]+peak_location[i+1])


def valleys(data):
    valley_location = []
#    #returns location of valleys
#    #a valley has higher numbers on BOTH SIDES
    for i in range(1, len(data)-1):
        left_side = data[i-1]
        right_side = data[i+1]
        mid = data[i]
        if left_side > mid and right_side > mid:
            valley_location.append(i)
    return valley_location
    #return valley_location[i-1:i+2], valley_location[i-1]+valley_location[i]+valley_location[i+1]

def peaks_and_valleys(data):
    peak = peaks(data)
    valley = valleys(data)
    return peak + valley

#    #compiles a list of both function above

def main():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    print(peaks(data))
    print(valleys(data))
    print(peaks_and_valleys(data))




