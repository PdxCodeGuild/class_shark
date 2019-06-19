#
# def common_elements(list1, list2):
#     common = []
#     for element in list1:
#         if element in list2 and element not in common:
#             common.append(element)
#     return common
#
# def common_items(list1, list2):
#     return [item for item in list1 if item in list2]
#
# def common_set_items(list1, list2):
#     set1 = set(list1)
#     set2 = set(list2)
#
#     return list(set1 & set2)
#
# print(common_elements([1, 2, 3, 4, 5], [1, 3, 5, 6, 7, 8]))
# print(common_elements(['red', 'blue', 'green'], ['blue', 'purple', 'pink']))
# print(common_items([1, 2, 3, 4, 5], [1, 3, 5, 6, 7, 8]))
# print(common_items(['red', 'blue', 'green'], ['blue', 'purple', 'pink']))
#
# print(common_set_items([1, 2, 3, 4, 5], [1, 3, 5, 6, 7, 8]))
# print(common_set_items(['red', 'blue', 'green'], ['blue', 'purple', 'pink']))

# dictionary problem 1
def combine(keys, values):

    combine_key_value = dict(zip(keys, values))

    return combine_key_value

def average(d):
    count = 0
    total_values = 0
    for i in d:
        count += 1
        total_values += d[i]
    return total_values / count 
    # to round average return float{'0: .2f}'.format(total / count))
    # return sum(d.values()) / len(d)

fruit = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]

print(combine(fruit, prices))
print(average(combine(fruit, prices)))

# dictionary problem 2
