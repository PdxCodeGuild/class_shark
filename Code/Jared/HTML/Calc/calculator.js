
// selectors
const display = document.querySelector('#display')
const digits = document.querySelectorAll('.number')
const operators =document.querySelectorAll('.symbol')
const decimal = document.querySelector('#dec')
const equal = document.querySelector('#equal')
const ce = document.querySelector('ce')
const ac = document.querySelector('ac')

// variables
let ans = 0
let operation = []
let op = null
let currentNumber = ''

function calculate(a, op, b){
	if (op === '+'){
		return a + b
	}else if (op === '-'){
		return a - b
	}else if (op === '*'){
		return a * b
	}else if (op === '/'){
		return a / b
	}
}

// event listeners

for (let digit of digits) {
	digit.addEventListener('click', (evt) =>{
		currentNumber += digit.innerText
		display.innerText = currentNumber
	})
}

decimal.addEventListener('click', (evt)=>{
	isDecimal = true
	if (!isDecimal) {
	currentNumber += '.'
	display.innerText = currentNumber
	}
})
for (let operator of operators){
	operator.addEventListener('click', (evt) =>{
		if (op) {
			ans = calculate(ans, op, currentNumber)
		}
		
		op = operator.innerText
		operation.push(parseFloat(currentNumber))
		operation.push(op)
		currentNumber = ''
		isDecimal = false
		display.innerText = op
	})
}