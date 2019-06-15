from random import randint


class Number_To_String():

    nts_str = ''
    d_to_alpha = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                  6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
                  11: 'eleven', 12: 'twelve', 13: 'thirteen', 20: 'twenty',
                  30: 'thirty', 40: 'fourty', 50: 'fifty', 60: 'sixty',
                  70: 'seventy', 80: 'eighty', 90: 'ninety'}

    def num_to_str(self, num):
        # 14-19 = four - teen
        # 40,60-90 = four - ty
        t_num = (num - (num % 100))
        if num < 100:
            self.nts_str += self.tens(num % 100)
        if num > 99:
            self.nts_str += (self.d_to_alpha[t_num / 100] + '-hundred')
            if (num % 100) != 0:
                self.nts_str += ('-' + self.tens(num % 100))

        return self.nts_str

    def tens(self, num):
        tens_str = ''
        if num < 14:
            tens_str += self.d_to_alpha[num]
        elif 13 < num < 20:
            tens_str += (self.d_to_alpha[num-10] + 'teen')
        else:
            tens_str += self.d_to_alpha[num - (num % 10)]
            if (num % 10) > 0:
                tens_str += ('-' + self.d_to_alpha[num % 10])
        return tens_str


def num_to_time(num):
    minutes = num % 100
    hours = (num - (num % 100)) / 100
    nts = Number_To_String()
    if hours > 0:
        t_str = nts.tens(hours)
    else:
        t_str = nts.tens(12)
    if minutes > 0:
        t_str += ' ' + nts.tens(minutes)
    return t_str + ' o\'clock'


def roman(num):
    d_rmn = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    s_rmn = ''
    t_num = num
    ls_num = list(str(num))
    # li_num = [int(x) for x in ls_num]
    # li_num.reverse()






def test_nts():
    for i in range(20):
        nts = Number_To_String()
        num = randint(0, 999)
        print(num)
        print(nts.num_to_str(num))


def test_time():
    TF = True
    while TF:
        time = int(input('time please: '))
        if ((time % 100) < 59) or (((time - (time % 100))/100) < 13):
            print(num_to_time(time))
            choice = input('again?').strip().lower()
            if choice.startswith('n'):
                TF = False
        else:
            print('invalid time')


def main():
    test_nts()
    test_time()


main()
