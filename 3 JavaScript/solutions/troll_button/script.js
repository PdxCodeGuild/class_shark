// script.js
// selector
const button = document.querySelector('#btn')

function randomCoord() {
  return [Math.floor(Math.random() * (window.innerWidth - button.offsetWidth)),
          Math.floor(Math.random() * (window.innerHeight - button.offsetHeight))]
}

// event listeners
button.addEventListener('mouseover', function(event) {
  let [x, y] = randomCoord()
  button.style.left = `${x}px`
  button.style.top = `${y}px`
})

button.addEventListener('click', function() {
  alert('💰You win (nothing)!💰')
})