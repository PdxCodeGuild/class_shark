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


# def fill(i, j, l_data):
#     end = 0
#     s_graph = ''
#     for point in range(j, len(l_data)):
#         if i == l_data[point]:
#             end = point
#     if end > 0:
#         for a in range(i, end):
#             s_graph += ' 0 '
#     return s_graph


def y_draw(l_data):
    x = [x for x in range(0, len(l_data))]
    y = [y for y in range(max(l_data)+1, 0, -1)]
    print_out = ''
    for i in y:
        for j in x:
            # if l_data[j-1] > l_data[j] and i <= l_data[j]:
            #     print_out += fill(i, j, l_data)
            if i <= l_data[j]:
                print_out += ' X '
            else:
                print_out += '   '
        print_out += '\n'
    print(print_out)


# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
data = [4,5,6,7,8,9,8,7,6,5,6,7,8,9,8,7,6,7,8,9,8,7,6,5,4,3,4,5,6,7,8]
l_pv = peaks_and_valleys(data)
l_pv.sort()
print(y_draw(data))
print(data)
print(l_pv)
