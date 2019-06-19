import string


def encode(rot_i, usr_In):
    l_in = list(usr_In.strip())
    print(l_in)
    ciph = []
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    for letter in l_in:
        if letter.islower():
            ciph.append(lower[
                        (lower.find(letter) + rot_i) % 26])
        elif letter.isupper():
            ciph.append(upper[
                        (upper.find(letter) + rot_i) % 26])
        else:
            ciph.append(letter)

    return ''.join(ciph)


def decode(rot_i, usr_In):
    return encode(-rot_i, usr_In)


def dict_encode(rot_i, usr_In):
    translate = dict(zip(string.ascii_letters
                         , string.ascii_letters[rot_i:]
                         + string.ascii_letters[:rot_i]))
    cyph = ''
    for letter in usr_In:
        cyph += translate.get(letter, letter)
    return cyph
    # return ''.join([translate.get(letter, letter) for letter in usr_In])

TF = True
while TF:
    i_usr_rot = int(input('how much rot: '))
    s_usr_str = input('please enter a sentence to encode: ')
    cip = dict_encode(i_usr_rot, s_usr_str)

    print("Your string was:\n"
          , s_usr_str
          , '\nYour encoded message is:\n'
          , cip)

    choice = input('again? y/n ')
    if choice == 'n':
        TF = False
