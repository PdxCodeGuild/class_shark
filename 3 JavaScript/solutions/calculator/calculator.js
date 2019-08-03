// calculator.js

// selectors
const display = document.querySelector('#display')
const history = document.querySelector('#history')
const digits = document.querySelectorAll('.digit')
const operators = document.querySelectorAll('.op')
const decimal = document.querySelector('#dec')
const equal = document.querySelector('#eq')
const ce = document.querySelector('#ce')
const ac = document.querySelector('#ac')

// variables
let ans = null
let operation = []
let op = null
let currentNumber = ''
let isDecimal = false

// functions
function calculate(a, op, b) {
  if (op === '+') {
    return a + b
  } else if (op === '-') {
    return a - b
  } else if (op === '/') {
    return a / b
  } else if (op === '*') {
    return a * b
  }
}

function clearAndDisplay(value) {
  if (value === undefined) value = 0 
  currentNumber = ''
  isDecimal = false  
  if (typeof value === 'number') {
    if (value % 1 || value > 99999999) { // if value is a float or large int, set precision
      value = value.toPrecision(10)
    }
  }
  display.innerText = value
  history.innerText = operation.join('')
}

function addDigit(digit) {
    currentNumber += digit
    display.innerText = currentNumber  
}

function addDecimal() {
  if (!isDecimal) {
    currentNumber += '.'
    display.innerText = currentNumber
    isDecimal = true
  }  
}

function addOperator(operator) {
  if (op && currentNumber) {
    ans = calculate(ans, op, parseFloat(currentNumber))
  } else if (!ans && ans !== 0) {
    ans = (currentNumber ? parseFloat(currentNumber) : 0)
  }
  op = operator
  if (currentNumber) operation.push(parseFloat(currentNumber))
  operation.push(op)
  clearAndDisplay(op)
}

function equals() {
  if (currentNumber) {
    operation.push(parseFloat(currentNumber))
    ans = calculate(ans, op, parseFloat(currentNumber))
  }
  clearAndDisplay(ans)  
}

function clearAll() {
  ans = 0
  operation = []
  op = null
  clearAndDisplay(ans)  
}

// event listeners

// digits.forEach((digit) => {
//   digit.addEventListener('click', (evt) => {
//     display.innerText = digit.innerText
//   })
// })

for (let digit of digits) {
  digit.addEventListener('click', (evt) => {
    addDigit(digit.innerText)
  })  
}

decimal.addEventListener('click', (evt) => {
  addDecimal()
})  

for (let operator of operators) {
  operator.addEventListener('click', (evt) => {
    addOperator(operator.innerText)
  })
}

equal.addEventListener('click', (evt) => {
  equals()
})

ce.addEventListener('click', (evt) => {
  clearAndDisplay(ans)
})

ac.addEventListener('click', (evt) => {
  clearAll()
})

window.addEventListener('keyup', evt => {
  console.log(evt)
  if (!isNaN(evt.key)) {
    addDigit(evt.key)
  } else if ('+-*/'.includes(evt.key)) {
    addOperator(evt.key)
  } else if (evt.key === '.') {
    addDecimal()
  } else if (['=', 'Enter'].includes(evt.key)) {
    equals()
  } else if (evt.key === 'Backspace') {
    clearAndDisplay()
  } 
})