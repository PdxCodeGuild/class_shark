const numBtns = document.querySelectorAll('.num-btn')
const operBtns = document.querySelectorAll('.operators')
const ce = document.querySelector('#ce')
const ac = document.querySelector('#ac')
const equals = document.querySelector('#eq')
const display = document.querySelector('#display')
const decimal = document.querySelector('#dec')

let operands = []
let currentNum = ''
let op = ''
let isDecimal = false


numBtns.forEach((button)=>{button.addEventListener('click', (evt) =>{
	currentNum += button.innerText
	display.innerText = currentNum
} )})

operBtns.forEach((button)=>{button.addEventListener('click', (evt) =>{
	operand.push(parseFloat(currentNum))
	op = button.innerText
	operand.push(op)
	currentNum = ''
	isDecimal = false
	display.innerText = op

} )})

decimal.addEventListener('click', (evt) =>{
	if (!isDecimal) {
	currentNum += button.innerText
	display.innerText = currentNum
	isDecimal = true;
	}
})