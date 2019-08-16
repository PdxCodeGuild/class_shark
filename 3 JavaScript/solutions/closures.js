/* closures.js

Here's a pretty good guide on closures in JS (https://wsvincent.com/javascript-scope-closures/)

JS (and Python) resolve variables in the following order:
LEG    L ocal
       E nclosing
       G lobal

If the program can't find a variable in the local scope, it will look up a level to any enclosing scopes, until finally the global scope. If it can't find the variable, you get a ReferenceError (NameError in Python).

Closures are nested functions. The inner function has access to the outer function(s) variables, because the other function(s) are the /enclosing/ scope.
*/

const name = 'barbara' // global

function outer() {
  const name = 'bobra' // local to outer()

  function inner() {
    // there is no local name variable in inner(), so the program checks the enclosing scope and grabs name from outer()
    console.log(name)
  }

  inner()
}

outer()             // prints bobra
console.log(name)   // prints barbara ('bobra' is not accessible in this scope)
// inner()             // ReferenceError (inner() is not accessible in this scope)


/*
Closures are used a lot in the wild.
Common uses include:
- creating function factories: a function that generates similar functions
- creating private variables

Below is an example of using a closure to generate similar (but different) functions.
*/

function powers_of(n) {
  /* returns a function that generates an array of the first q powers of n
  */
                          // [n**num for num in range(q)] python equivalent
  const quantity = (q) => [...Array(q).keys()].map(num => n**num)
  return quantity // notice how we don't call the inner function, but return it instead
}

// functions we create using the factory powers_of()
const powers_of_two = powers_of(2) 
const powers_of_three = powers_of(3)
const powers_of_ten = powers_of(10)

// use
console.log(powers_of_two(10)) // [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
console.log(powers_of_three(5)) // [1, 3, 9, 27, 81]
console.log(powers_of_ten(6)) // [1, 10, 100, 1000, 10000, 100000]

// the following are equivalent to lines 49-57
console.log(powers_of(2)(10)) // [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
console.log(powers_of(3)(5)) // [1, 3, 9, 27, 81]
console.log(powers_of(10)(6)) // [1, 10, 100, 1000, 10000, 100000]