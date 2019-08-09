// calculator.js

// vue app
const app = new Vue({
  el: '#calc-body',
  data: {
    display: null,
    history: [],
    ans: null,
    op: null,
    currentNumber: '',
    isDecimal: false,
    symbols: {
      '+': 'add',
      '-': 'sub',
      '×': 'mult',
      '*': 'mult',
      '÷': 'div',
      '/': 'div',   
      '.': 'dec',
      '=': 'eq',
      'Enter': 'eq',
      'CE': 'ce',
      'AC': 'ac'
    }  
  },
  methods: {
    calculate: function() {
      // ans op currentNumber, if the currentNumber exists
      if (this.currentNumber) {
        this.currentNumber = parseFloat(this.currentNumber)
        this.history.push(this.currentNumber)
        this.ans = (this.ans !== null ? this.ans : 0)
        if (this.op === '+') {
          this.ans += this.currentNumber
        } else if (this.op === '-') {
          this.ans -= this.currentNumber
        } else if (this.op === '*' || this.op === '×') {
          this.ans *= this.currentNumber
        } else if (this.op === '/' || this.op === '÷') {
          this.ans /= this.currentNumber
        }
      }
      this.clearEntry()
    },
    clearEntry: function() {
      this.currentNumber = ''
      this.isDecimal = false
      this.display = this.ans      
    },
    allClear: function() {
      this.ans = null
      this.history = []
      this.op = null
      this.clearEntry()
    },
    addDigit: function(digit) {
      this.currentNumber += digit
      this.display = this.currentNumber
    },
    addDecimal: function() {
      if (!this.isDecimal) {
        this.currentNumber += '.'
        this.isDecimal = true
        this.display = this.currentNumber
      }  
    },
    addOperator: function(operator) {
      if (!this.currentNumber && 
          isNaN(this.history[this.history.length-1]) && 
          operator === '-') {
            this.currentNumber = '-'
      } else {
        // if an operator is already set, calculate ans op currentNumber
        if (this.op) {
          this.calculate()
        // else if no ans is set, set ans as currentNumber or 0 if currentNumber is null
        } else if (!this.ans && this.ans !== 0) {
          this.ans = (this.currentNumber ? parseFloat(this.currentNumber) : 0)
        }
        this.op = operator
        // add currentNumber and operator to history
        if (this.currentNumber) this.history.push(parseFloat(this.currentNumber))
        this.history.push(this.op)
        // display the operator
        this.clearEntry()
        this.display = operator    
        }  
    },
    handleDigitClick: function(event) {
      const digit = event.target.innerText
      this.addDigit(digit)
    },
    handleOperatorClick: function(event) {
      const op = event.target.innerText
      this.addOperator(op)
    },
  },
  computed: {
    formattedHistory: function() {
      const history = this.history.join('')
      return history.length > 17 ? '...'+history.slice(-20) : history
    },
    formattedDisplay: function() {
      // format number so it doesn't overflow the display
      // display operators and null/empty values as is
      if (this.display in this.symbols ||
          this.display === '' || 
          this.display === null) {
            return this.display
      }

      let value = parseFloat(this.display)
      // if value is a large int, set precision
      if (value > 99999999) { 
        return value.toPrecision(8)      
      }

      // if value is a float, set precision and trim trailing 0s
      if (value % 1 ) {
        return parseFloat(value.toPrecision(8))
      }

      // return number if it needs no formatting
      return value
    }
  },
  mounted: function() {

    // keypress event listener to enable keyboard input
    window.addEventListener('keydown', evt => {
      // set logic for specific keys
      if (!isNaN(evt.key)) { // digits 
        // style button with corresponding key
        let button = document.querySelector(`#btn-${evt.key}`)
        button.classList.add('active')
        this.addDigit(evt.key)
      } else {
        // style button with corresponding key
        let button = document.querySelector(`#${this.symbols[evt.key]}`)
        if (button) button.classList.add('active')
        if ('+-*/'.includes(evt.key)) { // operators
          this.addOperator(evt.key)
        } else if (evt.key === '.') { // decimal
          this.addDecimal()
        } else if (['=', 'Enter'].includes(evt.key)) { // = or enter
          this.calculate()
        } else if (evt.key === 'Backspace') { // backspace
          this.clearEntry()
        }
      } 
    })

    window.addEventListener('keyup', evt => {
      // handle digits separately, since they have different selectors
      if (!isNaN(evt.key)) { // digits 
        let button = document.querySelector(`#btn-${evt.key}`)
        if (button) button.classList.remove('active')
      } else {
        let button = document.querySelector(`#${this.symbols[evt.key]}`)
        if (button) button.classList.remove('active')
      }
    })
  }
})
