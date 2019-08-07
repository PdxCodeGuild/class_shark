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

// selectors
const todoInput = document.querySelector('input[name="todo-text"]')
const addBtn = document.querySelector('#btn-add')
const listHolder = document.querySelector('.holder')

// functions
function update() {
  listHolder.innerHTML = ''
  for (let todo of todolist.todos) {
    let todoElement = document.createElement('li')
    let deleteBtn = document.createElement('i')
    let toggleBtn = document.createElement('i')
    // set text as todo.text and add completed class if todo.completed
    todoElement.innerText = todo.text
    if (todo.completed) todoElement.classList.add('completed')  
    // attach font awesome classes
    deleteBtn.classList.add('fas')
    deleteBtn.classList.add('fa-times')
    toggleBtn.classList.add('fas')
    toggleBtn.classList.add('fa-check')
    // add event listeners to buttons
    deleteBtn.addEventListener('click', evt => {
      todolist.remove(todo.text)
      update()
    })
    toggleBtn.addEventListener('click', evt => {
      todolist.toggleComplete(todo.text)
      update()
    })
    // attach buttons to todo element
    todoElement.appendChild(deleteBtn)
    todoElement.appendChild(toggleBtn)
    // attach to DOM
    listHolder.appendChild(todoElement)
  }
}

function addTodo() {
  if (todoInput.value) {
    todolist.add(todoInput.value)
    update()
    todoInput.value = ''
  }
}

// initialize todo list
let todolist = new TodoList()

// event listeners
window.addEventListener('load', evt => {
  let cachedTodos = localStorage.getItem('todos')
  if (cachedTodos) {
    cachedTodos = JSON.parse(cachedTodos)
    todolist.todos = cachedTodos
    update()
  }
})

window.addEventListener('unload', evt => {
  let todosJSON = JSON.stringify(todolist.todos)
  localStorage.setItem('todos', todosJSON)
})

todoInput.addEventListener('keydown', (evt) => {
  if (evt.key === "Enter") {
    addTodo()
  }
})

addBtn.addEventListener('click', addTodo)