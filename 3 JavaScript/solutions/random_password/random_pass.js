/*// random_pass.js

Lab 6: generate a random password
*/

const characters = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM;,./@^'

// selectors
let passLengthInput = document.querySelector('input[name="pass_length"]')
let generateBtn = document.querySelector('#generate')

// event listeners
generateBtn.addEventListener('click', (event) => {
  console.log(event)
  n = passLengthInput.value
  let password = ''

  for (let i=0; i<n; ++i) {
    let idx = Math.floor(Math.random() * characters.length)
    password += characters[idx]
  }
  document.querySelector('#password').innerText = password

})

