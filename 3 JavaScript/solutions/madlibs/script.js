/* Lab 2: Mad Lib
given a series of words, generate a silly sentence
  "_____________! he said ________ as he jumped into his convertible
    exclamation            adverb
   ______ and drove off with his __________ wife."
    noun                          adjective
*/

// # get words from the user
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