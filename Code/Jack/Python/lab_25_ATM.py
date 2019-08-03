class ATM(object):
    """docstring for ATM."""

    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.transaction_history = []

    def check_balance(self):
        '''
        returns the account balance
        '''
        return f'{self.balance}'

    def deposit(self, amount):
        '''
        deposits the given amount in the account
        '''
        self.balance += amount
        self.transaction_history.append(f'user deposited ${amount}')

    def check_withdrawl(self, amount):
        '''
        returns True if the withdrawn amount won't put the account in the
        negative
        '''
        return (self.balance - amount >= 0)

    def withdraw(self, amount):
        '''
        withdraws the amount from the account and returns it
        '''
        if self.check_withdrawl(amount):
            self.balance -= amount
            self.transaction_history.append(f'user withdrew ${amount}')
            return amount
        else:
            print(f'Insufficient Funds:')
            self.transaction_history.append(f'Insufficient Funds:',
                                            f'user attempted to withdraw ${amount}')
            return 0

    def print_transations(self):
        '''
        For printing out the list of transactions.
        '''
        print('-'*61)
        for line in self.transaction_history:
            print(f'{line}')
        print('-'*20, 'end of transactions', '-'*20)


def deposit():
    while True:
        try:
            amount = int(input('How much to deposit: $').strip())
            break
        except ValueError:
            print('invalid input: Please enter a number')
    atm.deposit(amount)


def withdraw():
    while True:
        try:
            amount = int(input('How much to withdraw: $').strip())
            break
        except ValueError:
            print('invalid input: Please enter a number')
    return atm.withdraw(amount)


if __name__ == '__main__':
    atm = ATM()
    loop = True
    print(f'Welcome to the ATM!')
    while loop:
        while True:
            REPL = input(f'what would you like to do ((d)eposit, (w)ithdraw, (c)heck balance, (h)istory, e(x)it)?').strip().lower()
            if REPL in ['deposit', 'withdraw', 'check balance',
                        'history', 'exit', 'd', 'w', 'c', 'h', 'x']:
                break
        if REPL.startswith('d'):
            deposit()
        elif REPL.startswith('w'):
            cash = withdraw()
            print(f'You pulled out ${cash}')
        elif REPL.startswith('c'):
            print(f'Current Balance: ${atm.check_balance()}')
        elif REPL.startswith('h'):
            atm.print_transations()
        elif REPL.startswith('x'):
            loop = False
