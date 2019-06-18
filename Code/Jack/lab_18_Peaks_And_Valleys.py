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


def x_draw(l_data):
    print_out = ''
    rows = max(l_data) + 1
    print(rows)
    for i in range(rows, 0, -1):
        for num in l_data:
            if num >= i:
                print_out += ' X '
            else:
                for j in find_peaks(l_data):
                    if i > j:
                        print_out += ' O '
                    else:
                        print_out += '   '
        print_out += '\n'
    return print_out


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
l_pv = peaks_and_valleys(data)
l_pv.sort()
print(x_draw(data))
print(data)
print(l_pv)
