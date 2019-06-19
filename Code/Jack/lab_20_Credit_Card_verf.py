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
        if self.i_chk_d == sum(self.li_ccn):
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
                self.li_ccn -= 9

    def get_valid(self):
        return self.valid
