// ATM
const vm = new Vue({
	el: '#container',

	data: {
		message: 'ATM',
		balance: 0,
		// account: [],
		selected: '',
		amount: '',
		accountBalance: null,
	},
	methods: {

		checkBalance: function(){
			// if (this.selected === 'checkBalance'){
				this.accountBalance = this.balance
			// }
		},

		deposit: function(){
			// if(this.selected === 'deposit'){
			this.balance += this.amount;
			this.checkBalance()
			// this.account.push(amount);
			// }
		},

		withdraw: function(){
		// 	if (this.selected === 'withdraw'){
		// }
			if (!(this.checkWithdrawal())){
				console.log("Insufficient Funds")
			}
			this.checkBalance()
		// 	if (this.balance <= 0){
		// 		return 'Insufficient Funds'
		// 	} else {
		// 		return this.balance
		// 	}
			// this.account.pop(amount);
		},

		checkWithdrawal: function(){
			if (this.balance - this.amount >= 0){
				this.balance -= this.amount
			}
		},

		select: function(){
			if (this.selected === 'checkBalance'){
				return this.checkBalance()
			} else if (this.selected === 'deposit'){
				return this.deposit()
			} else if (this.selected === 'withdraw'){
				return this.withdraw()
			}
		},

		clearEntry: function(){
			this.amount = ''
			this.accountBalance = null
			this.selected = ''
		},
	}
});


// // creat Balance class
// class ATM {
// 	constructor(balance=0, account) {
// 		this.balance = balance;
// 		this.account = []
// 	}
// 	// getBalance(){
// 	// 	return this.balance
// 	// }
	
// 	checkBalance(){
// 		return `Balance is ${this.balance}`
// 	}

// 	deposit(amount){
// 		this.balance += amount;
// 		this.account.push(amount);
// 		return this.balance
// 	}

// 	withdraw(amount) {
		
// 		this.balance -= amount;
// 		this.account.pop(amount);
// 			return this.balance
// 	}

// 	checkWithdrawal(amount){
// 		let check = this.balance -= amount;
// 		if (check > 0){
// 			return true
// 		}
// 	}
// }
// let account = new ATM()
// // let account = this.account
// console.log(account);
// account.deposit(100)
// console.log(account.checkBalance());
// account.withdraw(50);
// console.log(account.checkBalance());
// account.checkWithdrawal(75);
// console.log(account.checkBalance());
// console.log(account)
// // while true {

// }

