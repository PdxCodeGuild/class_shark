# Convert number to phrase

def num_phrase(num):
    ones_digit = num % 10
    tens_digit = num // 10

    ones = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    tens = {0: '', 1: 'ten', 2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety', 10: 'one-hundred'}

    if  tens_digit == 0:
        return ones[ones_digit]
    else:
        return tens[tens_digit] + ones[ones_digit]


def teen_phrase(num):
    teens = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    if 10 < num < 20:
        return teens[num]

while True:
    num = int(input("Enter a number between 1 and 100: "))

    if num == 0:
        print('zero')
    elif 10 >= num or num > 20:
        print(num_phrase(num))
    elif 11 < num < 20:
        print(teen_phrase(num))
        break
    print('-' * 60)
# print(teen_phrase(""))
# print(num_phrase('', ''))


#
# print(num_phrase(2))
# print(num_phrase(5))
