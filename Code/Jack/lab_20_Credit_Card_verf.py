class CreditCardValid(object):
    """docstring for CreditCardValid."""

    li_ccn = []
    i_chk_d = 0
    valid = False

    def __init__(self, s_ccn):
        super(CreditCardValid, self).__init__()
        self.li_ccn = list(s_ccn)
        self.str_to_int()
        self.li_ccn.reverse()
        self.i_chk_d = self.li_ccn.pop(0)
        self.double_ev_other()
        self.sub_nine()
        t_sum = sum(self.li_ccn)
        t_sum %= 10
        if self.i_chk_d == t_sum:
            self.valid = True

    def str_to_int(self):
        for i in range(len(self.li_ccn)):
            self.li_ccn[i] = int(self.li_ccn[i])

    def double_ev_other(self):
        for i in range(len(self.li_ccn)):
            if i % 2 == 0:
                self.li_ccn[i] *= 2

    def sub_nine(self):
        for i in range(len(self.li_ccn)):
            if self.li_ccn[i] > 9:
                self.li_ccn[i] -= 9

    def get_valid(self):
        return self.valid


user_credit_card_number = '4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'
user_credit_card_number = user_credit_card_number.replace(' ', '')
print(user_credit_card_number)
credit_card = CreditCardValid(user_credit_card_number)
if credit_card.get_valid():
    print('Your credit card is Valid!')
else:
    print('Your credit card is INvalid! get outta HERE!!!')
