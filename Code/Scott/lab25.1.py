"""
Name:           Scott Tran
Date            7/2/2019
Assignment:     Let's represent an ATM with a class containing a balance property. A newly created account will default to a balance of 0

"""
from pprint import pprint

class ATM:
    
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance 
        self.transactions = []

    def check_balance(self):
        print(f"{self.name}'s bank balance is {self.balance}.")

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} deposits {amount} into their account.")
        self.transactions.append(f"{self.name} deposited ${amount}")
    
    def withdrawal(self, amount):
        self.balance -= amount
        print(f"{self.name} withdraws {amount} into their account.")
        self.transactions.append(f"{self.name} withdrew ${amount}")
    
    def check_withdrawal(self, amount):
        print(f"Do I have enough to withdraw {amount}")
        if self.balance - amount > 0:
            print(True)
        else:
            print(False)

    def print_transactions(self):
        print(self.transactions)

p1 = ATM("Scott")

p1.check_balance()
p1.deposit(100)
p1.check_balance()
p1.check_withdrawal(200)
p1.withdrawal(50)
p1.check_balance()
p1.print_transactions