# lab13_rot13.py

abc = "abcdefghijklmnopqrstuvwxyz"


def rt13(x):

    return "".join([abc[(abc.find(c) + 13) % 26] for c in x])


phrase = "i am going crazy"
print(rt13(phrase))
print(rt13(rt13(phrase)))

# def rot13(x):
