'''
Lab 25: ATM
Let's represent an ATM with a class containing a balance property. A newly created account will default to a balance of 0. Implement the initializer, as well as the following methods:

check_balance() returns the account balance
deposit(amount) deposits the given amount in the account
check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
withdraw(amount) withdraws the amount from the account and returns it

Version 2
Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. Add a new function print_transactions() to your class for printing out the list of transactions.

Version 3
Allow the user to enter commands into a REPL.

> what would you like to do (deposit, withdraw, check balance, history)?
> deposit
> how much would you like to deposit?
> $5
> what would you like to do (deposit, withdraw, check balance, history)?
> check balance
> balance: $5
'''


'''
Lab 25: ATM
Let's represent an ATM with a class containing a balance property. A newly created account will default to a balance of 0. Implement the initializer, as well as the following methods:

check_balance() returns the account balance
deposit(amount) deposits the given amount in the account
check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
withdraw(amount) withdraws the amount from the account and returns it
'''
commands = ['c', 'check', 'check balance','check your balance', 'd', 'deposit funds', 'deposit', 'w', 'withdraw', 'withdraw funds', 'l', 'list', 'list transactions', 'list the transactions', 'list all', 'list all transactions', 'e', 'x', 'exit']


print('Welcome to Lab 24: ATM. A program coded in python by Caleb Mealey.')
print('In this lab we will represent an ATM using a class containing a balance property. The user will be allowed to check the balance, deposit funds, withdraw funds if funds are available, and log every ATM transaction.')
print('')


class ATM():
    '''
    class for implementation of CRUD REPL, allows the user to interact with the program and saved .csv file containing the bank account balance
    '''


    def __init__(self):
        '''
        initializer for the class
        '''
        self.balance = 0
        self.transaction_hist = []
        self.main_menu()


    def withdraw_check(self, withdraw_amt):
        '''
        '''
        if withdraw_amt > self.balance:
            return False
        else:
            return True
    
    def withdraw(self):
        '''
        '''
        withdraw_amt = int(input('Enter the amount you would like to withdraw from your account: '))
        if self.withdraw_check(withdraw_amt):
            self.balance -= withdraw_amt
            self.check_balance()
            self.transaction_hist.append(f'Customer withdrew ${withdraw_amt}')
            print(f'You successfully withdrew ${withdraw_amt}')
        else:
            print(f'You currently do not have enough funds to withdraw the amount of ${withdraw_amt}')
        pass


    def deposit(self):
        '''
        '''
        dep_amt = int(input('Enter the amount you would like to deposit: $'))
        self.balance += dep_amt
        self.transaction_hist.append(f'Customer deposited ${dep_amt}')
        print(f'You have successfully deposited ${dep_amt} into your account.')
        pass

    
    def check_balance(self):
        '''
        '''
        print(f'The current balance in the account is: ${self.balance}')
        pass
        
    
    def list_transactions(self):
        '''
        '''
        print(self.transaction_hist)
        pass

    def main_menu(self):
        '''
        Main Menu Logic & Display Instructions
        '''
        print('---' * 50)
        print('You can (c)heck your balance, (d)eposit funds, (w)ithdraw funds, (l)ist the transactions, or e(x)it')
        user_command = input('Enter your selection here: ').strip().lower()
        print('---' * 50)
        active_session = True
        while active_session:
            if user_command in commands:
                if user_command == 'c' or user_command.startswith('c'):
                    active_session = False
                    self.check_balance()
                    self.main_menu()
                    pass
                elif user_command == 'd' or user_command.startswith('d'):
                    active_session = False
                    self.deposit()
                    self.main_menu()
                    pass
                elif user_command == 'w' or user_command.startswith('w'):
                    active_session = False
                    self.withdraw()
                    self.main_menu()
                    pass
                elif user_command == 'l' or user_command.startswith('l'):
                    active_session = False
                    self.list_transactions()
                    self.main_menu()
                    pass
                elif user_command == 'x' or user_command.startswith('e'):
                    active_session = False
                    print('Thanks for using my ATM program!')
                    break
            


if __name__ == "__main__":
    ATM()
