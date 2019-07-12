#Lab 25 ATM
#check_balance() returns the account balance
#deposit(amount) deposits the given amount in the account
#check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
#withdraw(amount) withdraws the amount from the account and returns it

class ATM(object):

    def __init__(self, name, balance = 0, air = 2.5):
        self.name = name
        self.balance = balance
        self.annualinterestrate = air
        self.transactions = []

    def getname(self):
        return self.name

    def deposit(self, amount):
        '''
        this deposits the given amount in the account
        '''
        self.balance += amount
        self.transactions.append(f'Your deposited amount is:{amount}')
        #this is used for the transactions function
        return self.balance

    def withdraw(self, amount):
        #this will withdraw money from account
        self.transactions.append(f'You withdrew: {amount}')

        if amount <= self.balance:
            self.balance -= amount

        else:
            print("Insufficient Funds")

        return self.balance

    def check_balance(self):
        #this will check the user's balance

        print('-'*60)
        self.transactions.append(f'Your balance is: {self.balance}')
        #this is used to add to the transactions function
        return self.balance

    def check_withdrawal(self, amount):
        #this will check if a withdrawal amount will put your account in negative

        if amount <= self.balance:
            self.balance -= amount
            print (f'This ${amount} will not put your account in negative. You will have a {self.balance} Balance.')
        else:
            print("Insufficient Funds")

        self.transactions.append(f'You checked to withdraw: {amount}')

    def interest_calc(self):

        self.transactions.append(f'You gained ${self.balance * self.annualinterestrate} from their deposits')
        self.balance += self.annualinterestrate * self.balance

        return self.balance


    def print_transaction(self):
        #prints out all transactions

        for line in self.transactions:
            print(line)