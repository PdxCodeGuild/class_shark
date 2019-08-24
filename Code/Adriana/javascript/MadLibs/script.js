//Lab 2: Madlib

let exclamation = prompt('give me an exclamation! ')
let verb = prompt('give me a verb: ')
let noun = prompt('give me a noun: ')
let adjective = prompt('give me an adjective: ')

// # putting together the words into an output
// str concatenation
// let output = exclamation + '! he said ' + verb + ' as he jumped into his convertible '
// output += noun + ' and drove off with his ' + adjective + ' wife.'

// formatted str
let output = `"${exclamation}!," he said ${verb}ly, as he jumped into his convertible ${noun} and drove off with his ${adjective} wife.`

// # print the output
alert(output)