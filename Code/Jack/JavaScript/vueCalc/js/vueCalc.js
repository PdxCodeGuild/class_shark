// calculator.js


// vue version
const calcApp = new Vue({
  el: '#calcApp',
  data: {
    display: '',
    history: [],
    ans: null,
    op: null,
    curNum: '',
    isDecimal: false,
  },
  methods: {
    calculate: function(){
      // and + cur if cur exsists
      if (this.curNum) {
        this.history.push(parseFloat(this.curNum))
        console.log(this.curNum)
        this.history.push(this.op)
        this.ans = (this.ans !== null ? this.ans : 0)
        console.log(this.op)
        if (this.op === '+') {
          this.ans += this.curNum
        } else if (this.op === '-') {
          this.ans -= this.curNum
        } else if (this.op === '*' || this.op === '×') {
          this.ans *= this.curNum
        } else if (this.op === '/' || this.op === '÷') {
          this.ans /= this.curNum
        }
        console.log('ans', this.ans)
        this.clearEntry()
      }
    },

    clearEntry: function() {
      this.curNum = ''
      this.display = this.ans
    },

    allClear: function() {
      this.clearEntry()
      this.history = []
      this.ans = null
      this.op = null
    },

    addDigit: function(digit) {
      this.curNum += digit
      console.log('look here', this.curNum)
      this.display = this.curNum
    },

    addDec: function() {
      if (!this.isDecimal) {
        this.curNum += '.'
        this.isDecimal = true
      }
    },

    addOp: function(op) {
      this.op = op
      this.display = this.op
      this.calculate()

    },

    handleDigit: function(event) {
      const digit = event.target.innerText
      this.addDigit(digit)
    },

    handleOp: function(event) {
      const t_op = event.target.innerText
      this.addOp(t_op)
    }
  }

})



// // selectors
// const display = document.querySelector('#display')
// const history = document.querySelector('#history')
// const digits = document.querySelectorAll('.digit')
// const operators = document.querySelectorAll('.op')
// const decimal = document.querySelector('#dec')
// const equal = document.querySelector('#eq')
// const ce = document.querySelector('#ce')
// const ac = document.querySelector('#ac')

// // variables
// let operation = []      // history of operations
// let ans = null          // current answer
// let op = null           // current operator
// let currentNumber = ''  // current number
// let isDecimal = false   // decimal flag
// const symbols = {
//   '+': 'add',
//   '-': 'sub',
//   '×': 'mult',
//   '*': 'mult',
//   '÷': 'div',
//   '/': 'div',   
//   '.': 'dec',
//   '=': 'eq',
//   'Enter': 'eq',
//   'CE': 'ce',
//   'AC': 'ac'
// }

// // functions

// // computes a op b
// function calculate(a, op, b) {
//   if (op === '+') {
//     return a + b
//   } else if (op === '-') {
//     return a - b
//   } else if (op === '*' || op === '×') {
//     return a * b
//   } else if (op === '/' || op === '÷') {
//     return a / b
//   }
// }

// // resets currentNumber and isDecimal and displays value and history onscreen
// function clearAndDisplay(value) {
//   if (value === null) value = 0 
//   currentNumber = ''
//   isDecimal = false  

//   // format number so it doesn't overflow the display
//   // if value is a float, set precision and trim trailing 0s
//   if (value % 1 ) {
//     value = parseFloat(value.toPrecision(8))
//   }
//   // if value is a large int, set precision
//   if (value > 99999999) { 
//     value = value.toPrecision(8)      
//   }
//   // display value and history onscreen
//   display.innerText = value
//   history.innerText = operation.join('')
// }

// // adds digit to currentNumber and displays it onscreen
// function addDigit(digit) {
//     currentNumber += digit
//     display.innerText = currentNumber  
// }

// // adds decimal to currentNumber
// function addDecimal() {
//   if (!isDecimal) {
//     currentNumber += '.'
//     display.innerText = currentNumber
//     isDecimal = true
//   }  
// }

// // adds operator
// function addOperator(operator) {
//   // if an operator is already set, calculate ans op currentNumber
//   if (op && currentNumber) {
//     ans = calculate(ans, op, parseFloat(currentNumber))
//   // else if no ans is set, set ans as currentNumber or 0 if currentNumber is null
//   } else if (!ans && ans !== 0) {
//     ans = (currentNumber ? parseFloat(currentNumber) : 0)
//   }
//   op = operator
//   // add currentNumber and operator to history
//   if (currentNumber) operation.push(parseFloat(currentNumber))
//   operation.push(op)
//   // display the operator
//   clearAndDisplay(op)
// }

// // compute ans op currentNumber and display onscreen
// function equals() {
//   if (currentNumber) {
//     operation.push(parseFloat(currentNumber))
//     ans = (ans !== null ? ans : 0)
//     ans = calculate(ans, op, parseFloat(currentNumber))
//   }
//   clearAndDisplay(ans)  
// }

// // reset all values
// function clearAll() {
//   operation = []
//   ans = null
//   op = null
//   clearAndDisplay(ans)  
// }

// // event listeners

// // button event listeners

// // digits.forEach((digit) => {
// //   digit.addEventListener('click', (evt) => {
// //     display.innerText = digit.innerText
// //   })
// // })

// // same logic for each digit button
// for (let digit of digits) {
//   digit.addEventListener('click', (evt) => {
//     addDigit(digit.innerText)
//   })  
// }

// decimal.addEventListener('click', (evt) => {
//   addDecimal()
// })  

// // same logic for each operator button
// for (let operator of operators) {
//   operator.addEventListener('click', (evt) => {
//     addOperator(operator.innerText)
//   })
// }

// equal.addEventListener('click', (evt) => {
//   equals()
// })

// ce.addEventListener('click', (evt) => {
//   clearAndDisplay(ans)
// })

// ac.addEventListener('click', (evt) => {
//   clearAll()
// })

// // keypress event listener to enable keyboard input
// window.addEventListener('keydown', evt => {
//   console.log(evt)
//   // set logic for specific keys
//   if (!isNaN(evt.key)) { // digits 
//     // style button with corresponding key
//     let button = document.querySelector(`#btn-${evt.key}`)
//     button.classList.add('active')
//     addDigit(evt.key)
//   } else {
//     // style button with corresponding key
//     let button = document.querySelector(`#${symbols[evt.key]}`)
//     if (button) button.classList.add('active')
//     if ('+-*/'.includes(evt.key)) { // operators
//       addOperator(evt.key)
//     } else if (evt.key === '.') { // decimal
//       addDecimal()
//     } else if (['=', 'Enter'].includes(evt.key)) { // = or enter
//       equals()
//     } else if (evt.key === 'Backspace') { // backspace
//       clearAndDisplay(ans)
//     }
//   } 
// })

// window.addEventListener('keyup', evt => {
//   // handle digits separately, since they have different selectors
//   if (!isNaN(evt.key)) { // digits 
//     let button = document.querySelector(`#btn-${evt.key}`)
//     if (button) button.classList.remove('active')
//   } else {
//     let button = document.querySelector(`#${symbols[evt.key]}`)
//     if (button) button.classList.remove('active')
//   }
// })