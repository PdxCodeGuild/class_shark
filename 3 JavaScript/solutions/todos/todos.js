// todos.js
// selectors
const todoInput = document.querySelector('input[name="todo-text"]')
const addBtn = document.querySelector('#btn-add')
const listHolder = document.querySelector('.holder')

// functions
function addTodo() {
  if (todoInput.value) {
    // create todo li element in JS
    let todoElement = document.createElement('li')
    let deleteBtn = document.createElement('i')
    let toggleBtn = document.createElement('i')
    todoElement.innerText = todoInput.value
    // attach font awesome classes
    deleteBtn.classList.add('fas')
    deleteBtn.classList.add('fa-times')
    toggleBtn.classList.add('fas')
    toggleBtn.classList.add('fa-check')
    // add event listeners to button
    deleteBtn.addEventListener('click', evt => {
      // equivalent
      // let todo = deleteBtn.closest('li')
      // let todo = evt.target.closest('li')
      // let todo = evt.target.parentElement
      let todo = todoElement
      // remove todo from DOM
      listHolder.removeChild(todo)
    })
    toggleBtn.addEventListener('click', evt => {
      let todo = todoElement
      todo.classList.toggle('completed')
    })
    // add buttons to todo element
    todoElement.appendChild(deleteBtn)
    todoElement.appendChild(toggleBtn)
    // attach todo element to DOM
    listHolder.appendChild(todoElement)
    todoInput.value = ''
  }
}

// event listeners
todoInput.addEventListener('keydown', (evt) => {
  if (evt.key === "Enter") {
    addTodo()
  }
})

addBtn.addEventListener('click', addTodo)