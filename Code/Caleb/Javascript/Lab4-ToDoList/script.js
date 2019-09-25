// script.js
/* This is the primary javascript code for Lab 4 - To-Do List, programmed by Caleb Mealey in the PDX Code Guild Summer 2019 Full-Stack Developer Evening Course */
class ToDoList {
    constructor() {
        this.todos = []
    }

    add(text) {
        this.todos.push({text:todo, completed: false})
    }

    find(text) {
        return this.todos.filter(todo => todo.text === text)
    }

    remove(text) {
        let idx = this.todos.indexOf(todo)
        let removed = this.todos.splice(idx, 1)
        console.log(removed)
    }

    toggleComplete(text) {
        let idx = this.todos.indexOf(todo)
        this.todos[idx].completed = !this.todos[idx].completed
    }
}

// initialize To-Do List
let todolist = new ToDoList()

// selectors
const todoInput = document.querySelector('input[name='todolist''])
const addBtn = document.querySelector('#btn-add')
const listHolder = document.querySelector('.holder')

// event listeners
todoInput.addEventListener('keydown', (evt) => {
    if (evt.key === 'Enter') {
        todolist.add(todoInput.value)
        let todoElement = document.createElement('li')
        let deleteBtn = document.createElement('i')
        let toggleBtn = document.createElement('i')
        todoElement.innerText = todoInput.value
        deleteBtn.classList.add('fas')
        deleteBtn.classList.add('fa-times')
        toggleBtn.classList.add('fas')
        toggleBtn.Btn.classlist.add('fa-check')
        todoElement.appendChild(deleteBtn)
        todoElement.appendChild(toggleBtn)
        listHolder.appendChild(todoElement)
        todoInput.value = ''
    }
})