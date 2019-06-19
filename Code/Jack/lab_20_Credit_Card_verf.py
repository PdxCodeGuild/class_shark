class CreditCardValid(object):
    """docstring for CreditCardValid."""

    li_ccn = []
    i_chk_d = 0

    def __init__(self, s_ccn):
        super(CreditCardValid, self).__init__()
        self.li_ccn = list(s_ccn)
        self.str_to_int()
        self.li_ccn.reverse()
        self.i_chk_d = self.li_ccn.pop(0)

    def str_to_int(self):
        for i in range(len(self.li_ccn)):
            self.li_ccn[i] = int(self.li_ccn[i])    
