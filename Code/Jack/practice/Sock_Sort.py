import random


sock_Types = ['ankle', 'crew', 'calf', 'thigh']
sock_Colors = ['black', 'white', 'blue']
l_socks = [(random.choice(sock_Colors) + ' ' + random.choice(sock_Types))
           for i in range(100)]
# d_sock = {typ: 0 for typ in l_socks}
d_sock = {}
for sock in l_socks:
    # d_sock[sock] += 1
    d_sock[sock] = d_sock.get(sock, 0) + 1
print(d_sock)

for sock in counter:
    print(f'{sock} count = {counter[sock]}')
    if counter[sock] % 2:
        print('Throw away sock')
