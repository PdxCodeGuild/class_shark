//random password class example

const characters = '1234567890qwertyuiopasdfghklzxcvbnm'

let n = parseInt(prompt'(enter your'e desired password length:')
let password = ''

//for i in range(n):
//    password += random.choice(characters)
//print(password)

for (let i=0; i<n; ++i) {
    let idx = Math.floor(Math.random() *characters.length)
    password += characters[idx]

}

console.log(password))