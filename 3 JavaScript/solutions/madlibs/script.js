/* Lab 2: Mad Lib
given a series of words, generate a silly sentence
  "_____________! he said ______ as he jumped into his convertible
    exclamation            verb
   ______ and drove off with his ___________ wife."
    noun                          adjective
*/
// selecting input from DOM
const exc = document.querySelector('input[name="exclamation"]')
const v = document.querySelector('input[name="verb"]')
const n = document.querySelector('input[name="noun"]')
const adj = document.querySelector('input[name="adjective"]')
const madlib = document.querySelector('#madlib')
const generateBtn = document.querySelector('#generate')

//  putting together the words into an output 
// str concatenation
// formatted str
const output = () => {
  // get words from the user
  let exclamation = exc.value
  let verb = v.value
  let noun = n.value
  let adjective = adj.value
  // display the output onscreen
  madlib.innerText = `"${exclamation}!," he said ${verb}ly, as he jumped into his convertible ${noun} and drove off with his ${adjective} wife.`
}

// event listener
generateBtn.addEventListener('click', function(evt) {
  evt.preventDefault()
  output()
})

// event listener
generateBtn.addEventListener('mousemove', function(evt) {
  // if (evt.)
  console.log(evt)
  output()
})

