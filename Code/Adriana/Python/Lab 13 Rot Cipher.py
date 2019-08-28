#ROT13
import string

def rot13(text):

    alpha = 'abcdefghijklmnopqrstuvwxyz'
    rotated = 'nmopqrstuvwxyzabcdefghijklm'

    code = ''

    for letter in text:
        index = alpha.find(letter)
        code += rotated[index]
    return code

def rot(text, n):

    alpha = 'abcdefghijklmnopqrstuvwxyz'
    code = ''

    for letter in text:
        index = alpha.find(letter)
        index += n

        while index >= len(alpha):
            index -= len(alpha)
        code += alpha[index]

    return code

if __name__ == '__main__':

    print(rot(input("enter a string: "), int(input("enter your rotation offset: "))))

#Notes from class below:
#while user_choice in abc_list:
#if the word is in the abc list then run the below code:

    #for i in range(len(abc_list)):
    #    abc_list = rot_num + abc_list.index(user_choice)
     #   print(f"Your rotation is {abc_list[rotate]}")

#if user_choice in abc_list:
    #print("Its a letter")
    #print(f"Your position is: {abc_list.index(user_choice)}")
    #rotate = rot_num + abc_list.index(user_choice)
    #print(f"Your rotation is {abc_list[rotate]}")

#if user_choice in num_index:
    #print("Its a number")
    #user_choice = int(user_choice)*rot_num
    #print(abc_list[user_choice])
    #print(f"Your rotation is {user_choice}")