import string
abc_list = list(string.ascii_lowercase)
#this is the list of all lower case letters
num_index = list(string.digits)
#this is the list of the index
user_choice = list(input("What is  your word? "))
#user writes the word
rot_num = int(input("How much would you like to rotate?"))

while user_choice in abc_list:
#if the word is in the abc list then run the below code:
    for user_choice in abc_list:
        rotate = rot_num + abc_list.index(user_choice)
        print(f"Your rotation is {abc_list[rotate]}")