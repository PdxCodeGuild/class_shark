/*// random_pass.js

Lab 6: generate a random password
*/

const characters = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM;,./@^'
let n = 1

while (n) {
  n = parseInt(prompt('Enter your desired password length: '))
  let password = ''

  for (let i=0; i<n; ++i) {
    let idx = Math.floor(Math.random() * characters.length)
    password += characters[idx]
  }
  alert(password)
}
