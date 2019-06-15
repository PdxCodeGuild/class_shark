from random import randint


def number_to_string(num):
    # 14-19 = four - teen
    # 40,60-90 = four - ty

    nts_str = ''
    d_to_alpha = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'
                , 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'
                , 11: 'eleven', 12: 'twelve', 13: 'thirteen', 20: 'twenty'
                , 30: 'thirty', 40: 'fourty', 50: 'fifty', 60: 'sixty'
                , 70: 'seventy', 80: 'eighty', 90: 'ninety'}
    if num < 100:
        nts_str += tens(num % 100, d_to_alpha)
    if num > 99:
        nts_str += (d_to_alpha[(num - (num % 100)) / 100] + '-hundred')
        if (num % 100) != 0:
            nts_str += ('-' + tens(num % 100, d_to_alpha))

    return nts_str


def tens(num, d_to_alpha):
    tens_str = ''
    if num < 14:
        tens_str += d_to_alpha[num]
    elif 13 < num < 20:
        tens_str += (d_to_alpha[num-10] + 'teen')
    else:
        tens_str += d_to_alpha[num - (num % 10)]
        if (num % 10) > 0:
            tens_str += ('-' + d_to_alpha[num % 10])
    return tens_str


def num_to_time(num):
    pass

def main():
    for i in range(20):
        num = randint(0, 999)
        print(num)
        print(number_to_string(num))


main()
