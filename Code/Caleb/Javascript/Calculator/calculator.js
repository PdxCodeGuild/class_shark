// calculator.js

// selectors
const display = document.querySelector('#display')
const digits = document.querySelectorAll('.digit')
const operators = document.querySelectorAll('.op')
const decimal = document.querySelector('#dec')
const equal = document.querySelector('#eq')
const ce = document.querySelector('#ce')
const ac = document.querySelector('#ac')

// variables
let ans = 0
let lhs = rhs = op = ''

// event listeners


for (let digit of digits) {
    digit.addEventListener('click', (evt) => {
        lhs += digit.innerText
        display.innerText = lhs
    })
}

for (let op of operators) {
    op.addEventListener('click', (evt) => {
        display.innerText = op.innerText
    })
}