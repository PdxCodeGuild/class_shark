# sock_sorter.py
# from collections import defaultdict, Counter
import random

sock_types = ['ankle', 'crew', 'calf', 'thigh']
sock_colors = ['black', 'white', 'blue']
socks = []
counter = {}
# counter = dict(zip(sock_types, [*[0]*4]))
# # counter = dict(zip(sock_types, [0, 0, 0, 0]))
for i in range(100):
    sock_type = random.choice(sock_types)
    sock_color = random.choice(sock_colors)
    sock = (sock_type, sock_color)
    counter[sock] = counter.get(sock, 0) + 1
    # # equivalent to line above
    # if sock in counter:
    #     counter[sock] += 1
    # else:
    #     counter[sock] = 1
    socks.append(sock) 

# print(socks)
# print(counter)
# print(Counter(socks))
for sock in counter:
    print(f'{sock} count = {counter[sock]}')
    if counter[sock] % 2:
        print('throw away a sock')