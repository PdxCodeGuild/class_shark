"""
Name:           Scott Tran
Date            6/7/2019
Assignment:     Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average. 
"""
my_list = []


def num(x):
    while True:
        x = input("Please give me a number or type 'done' :")
        if x == 'done':
            break
        elif x.isdigit():
            my_list.append(int(x))
        else:
            print("That is not an integer number. Please try again.")
        

num(my_list)

print(my_list)

# def num(x):
#     while True:
#         try:
#             x = int(input("Please give me a number or type 'done' :"))
#             if x == 'done':
#                 break
#             else:
#                 my_list.append(x)
#         # else:
#         #     print("That is not an integer number.")
#         #     continue
#         except ValueError:
#             print("No valid integer! Please try again ...")


# num(my_list)

# print(my_list)
