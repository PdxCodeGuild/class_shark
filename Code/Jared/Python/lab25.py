# lab25.py

class Balance:

	def __init__(self, balance=0):
		self.balance = balance 
		self.transactions = []

	def __repr__(self):
		return str(self.balance)

	def check_balance(self):
		return f"Your balance is: {self.balance}."

	def deposit(self, amount): 
		self.balance += amount
		self.transactions.append(f'You deposited ${amount}')
		return self.balance
		
	def check_withdrawal(self, amount):
		check = self.balance - amount
		if check > 0:
			return True

	def withdraw(self, amount):
		self.balance -= amount
		self.transactions.append(f'You withdrew ${amount}')
		return self.balance

	def print_transactions(self):
		return self.transactions

		

if __name__ == '__main__':
	
	account = Balance()

	while True:

		user_action = input('Would you like to (d)eposit, (w)ithdraw, (c)heck balance, or see (h)istory?: ').lower()
			
		if user_action in ['d', 'deposit', 'w', 'withdraw', 'c', 'check balance', 'h', 'history']:
		
			if user_action in ['d', 'desposit']:
				amount = int(input('How much would you like to deposit: '))
				print(account.deposit(amount))
			elif user_action in ['w', 'withdraw']:
				amount = int(input('How much would you like to withdraw: '))
				if account.check_withdrawal(amount) == True:
					print(account.withdraw(amount))
				else:
					print('Insufficient funds')
			elif user_action in ['c', 'check balance']:
				print(account.check_balance())
			elif user_action in ['h', 'history']:
				print(account.print_transactions())

		
			more_transactions = input('Any further transacitons?: (y)es or (n)o: \n')	
			if more_transactions in ['y', 'yes']:
				more_transactions== True
			else:
				break
	
		else:
			print('Invalid entry.')


		




	