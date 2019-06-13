import string


def rot_Cipher(rot_i, usr_In):
    l_in = list(usr_In.strip())
    print(l_in)

    # ciph = [(string.ascii_letters[string.ascii_letters.find(letter)
    #         + rot_i - 52]) for letter in l_in]

    ciph = []
    for letter in l_in:
        if letter.islower():
            ciph.append(string.ascii_lowercase[
                        string.ascii_lowercase.find(letter)
                        + rot_i - 26])
        elif letter.isupper():
            ciph.append(string.ascii_uppercase[
                        string.ascii_uppercase.find(letter)
                        + rot_i - 26])
        else:
            ciph.append(' ')

    return ''.join(ciph)


TF = True
while TF:
    i_usr_rot = int(input('how much rot: '))
    s_usr_str = input('please enter a sentence to encode: ')
    cip = rot_Cipher(i_usr_rot, s_usr_str)
    cip = cip.replace('0', ' ')
    print("Your string was:\n", s_usr_str, '\nYour encoded message is:\n'
          , cip)
    choice = input('again? y/n ')
    if choice == 'n':
        TF = False
