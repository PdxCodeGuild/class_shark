// todos.js
class TodoList {
  constructor() {
    this.todos = []
  }
  
  add(text) {
    this.todos.push({text: text, completed: false})
  }

  find(text) {
    return this.todos.find(todo => todo.text === text)
  }

  remove(text) {
    let todo = this.find(text)
    let idx = this.todos.indexOf(todo)
    console.log(idx)
    let removed = this.todos.splice(idx, 1)
    console.log(removed)
  }

  toggleComplete(text) {
    let todo = this.find(text)
    let idx = this.todos.indexOf(todo)
    this.todos[idx].completed = !this.todos[idx].completed
  }
}

// initialize todo list
let todolist = new TodoList()

// selectors
const todoInput = document.querySelector('input[name="todo-text"]')
const addBtn = document.querySelector('#btn-add')
const listHolder = document.querySelector('.holder')

// functions
function addTodo() {
  if (todoInput.value) {
    todolist.add(todoInput.value)
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