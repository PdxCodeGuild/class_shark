# lab 10 Average Numbers

# version 1


# def average(nums):
#     count = 0 # count the number indeces
#     sum = 0 # create the sum of the values
#     for num in range(len(nums)):
#         count += 1
#         sum += nums[num]
#     return sum / count
# nums = [1, 2, 3, 4]
# print(average(nums))


# version 2

def average_input():
    nums = []

    while True:
        user_input = input("Enter a number, or 'done': ")
        if user_input == 'done':
            break
        else:
            nums.append(int(user_input))

    avg = sum(nums) / len(nums)

    return 'Average', avg



            #
            # aprint(type(nums))

        #


    #     sums = 0
    #     count = 0
    #     for i in range(nums):
    #         nums.append(user_input)
    #         sums = sum(nums)
    #
        # return nums


print(average_input())
