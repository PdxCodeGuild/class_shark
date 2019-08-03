def validate(nums):

    card_number = list(nums)
    card_number = [int(i) for i in card_number]
    print(card_number)

    # slice the last index for later check
    chk_num = card_number[:-1]
    print(chk_num)

    #reverse list
    rev_num = chk_num[::-1]
    print(rev_num)

    # double every item in reverse list
    for i in range(len(rev_num)):
        if i % 2 == 0:
            rev_num[i] = rev_num[i] * 2
    print(rev_num)

    # sub 9 from i > 9
    for num in range(len(rev_num)):
        if rev_num[num] > 9:
            rev_num[num] = rev_num[num] - 9
    print(rev_num)

    # sum of values
    sum_values = sum(rev_num)
    print(sum_values)

    # take second digit of sum
    str_values = str(sum_values)
    second_digit = int(str_values[1])
    print(second_digit)

    # check to see if second digit is same as early num check
    if second_digit == card_number[-1]:
        return 'Valid'
    else:
        return 'Invalid'

while True:
    user_input = input("Enter a 16 digit number made up of digits between 0-9: ")
    if len(user_input) != 16:
        print('Please enter 16 digits')
    else:
        break


print(validate(user_input))
