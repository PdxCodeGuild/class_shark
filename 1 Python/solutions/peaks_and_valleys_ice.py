# peaks_and_valleys.py
def peaks_or_valleys(peaks=True):
    '''
    :peaks: bool
    closure that returns a function for peaks or valleys based on the flag peaks
    '''
    def inner(heights):
        p_or_v = []
        for i in range(1, len(heights)-1): # shorten the range to ignore the first and last indices
            left = heights[i-1]
            mid = heights[i]
            right = heights[i+1]
            # print(i-1, i, i+1, left, mid, right)
            if peaks:
                if left < mid > right:
                    p_or_v.append(i)
            else:
                if left > mid < right:
                    p_or_v.append(i)
        return p_or_v
    return inner


def peaks(heights):
    '''
    :heights: list of ints
    returns the indices of valleys. A valley has a taller height than its left and right neighbors    
    '''
    return peaks_or_valleys()(heights)
    # p = []
    # for i in range(1, len(heights)-1):
    #     left = heights[i-1]
    #     mid = heights[i]
    #     right = heights[i+1]
    #     # print(i-1, i, i+1, left, mid, right)
    #     if left < mid > right:
    #         p.append(i)
    # return p


def valleys(heights):
    '''
    :heights: list of ints
    returns the indices of peaks. A peak has a lower height than its left and right neighbors    
    '''
    return peaks_or_valleys(peaks=False)(heights)
    # v = []
    # for i in range(1, len(heights)-1):
    #     left = heights[i-1]
    #     mid = heights[i]
    #     right = heights[i+1]
    #     # print(i-1, i, i+1, left, mid, right)
    #     if left > mid < right:
    #         v.append(i)
    # return v


def peaks_and_valleys(heights):
    '''
    :heights: list of ints
    returns list of the indices of peaks and valleys (sorted)
    '''    
    p = peaks(heights)
    v = valleys(heights)
    return sorted(p + v)


def draw(heights):
    '''
    :heights: list of ints
    draws mountain based on heights
    '''

    mountain = ''
    top = max(heights)
    current_height = top
    while current_height > 0:
        for height in heights:
            if height >= current_height:
                mountain += 'X'
            else:
                mountain += ' '
        mountain += '\n'
        current_height -= 1
    print(mountain)

def draw_water(heights):
    '''
    Imagine pouring water into onto the hills drawn from draw(). 
    The water would wash off the left and right sides, but would accumulate in the valleys. 
    Below the water is represented by O's.
    Draw the mountain with water.  
    '''
    p = [0] + peaks(heights) + [len(heights)-1]
    mountain = ''
    top = max(heights)
    current_height = top

    while current_height > 0:
        peak_idx = 0
        current_peak = p[peak_idx]
        next_peak = p[peak_idx + 1]
        water_height = min(heights[current_peak], heights[next_peak])

        for i, height in enumerate(heights):
            if i > next_peak:
                peak_idx += 1
                current_peak = next_peak
                next_peak = p[peak_idx+1]
                water_height = min(heights[current_peak], heights[next_peak])

            if height >= current_height:
                mountain += 'X'
            else:
                if current_peak < i < next_peak:
                    if water_height >= current_height:
                        mountain += 'o'
                    else:
                        mountain += ' '
                else:
                    mountain += ' '

        mountain += '\n'
        current_height -= 1
    print(mountain)    


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    # peaks = peaks_or_valleys()
    # valleys = peaks_or_valleys(peaks=False)
    print(peaks(data))    
    print(valleys(data))    
    print(peaks_and_valleys(data))
    draw(data)
    draw_water(data)