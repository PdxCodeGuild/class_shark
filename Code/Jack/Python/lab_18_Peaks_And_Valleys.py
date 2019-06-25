def find_peaks(l_data):
    tl_data = []
    for i in range(1, len(l_data)-1):
        if l_data[i-1] < l_data[i] > l_data[i+1]:
            tl_data.append(i)
    return tl_data


def find_valley(l_data):
    tl_data = []
    for i in range(1, len(l_data)-1):
        if l_data[i-1] > l_data[i] < l_data[i+1]:
            tl_data.append(i)
    return tl_data


def peaks_and_valleys(l_data):
    return find_peaks(l_data) + find_valley(l_data)


def find_end(i, j, l_data):
    #        5  0
    end = 0
    peak = l_data[j]  # [0] = 5
    # print('col:', j, 'row:', i, end, peak)
    # check to see if 'peak' is less than next
    j += 1  # [1] = 4
    if peak >= l_data[j]:
        for itr in range(j, len(l_data)):
            # 1           1      12
            if l_data[itr] == peak:
                end = itr
                return end
    return end


def y_draw(l_data):
    x = [x for x in range(0, len(l_data))]
    y = [y for y in range(max(l_data)+1, 0, -1)]
    print_out = ''
    peak = 0
    for i in y:
        end = 0
        for j in x:
            if j != len(l_data)-1:
                next = l_data[j + 1]
            else:
                next = l_data[j]
            if l_data[j] > next and l_data[j] >= i:
                if i > next:  # <- this was the conditional that I couldn't get
                    peak = j
                    end = find_end(i, j, l_data)
            if peak < j < end:
                print_out += ' 0 '
            elif i <= l_data[j]:
                print_out += ' X '
            else:
                print_out += '   '
        print_out += '\n'
    print(print_out)


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# data = [4,5,6,7,8,9,8,7,6,5,6,7,8,9,8,7,6,7,8,9,8,7,6,5,4,3,4,5,6,7,8]
# data = [5,4,3,4,5,6,5,4,3,2,3,4]
# data = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,4,3,2,1,2,3,4,5,6,7,8,9,8,7,6]
l_pv = peaks_and_valleys(data)
l_pv.sort()
print(y_draw(data))
print(data)
print(l_pv)
