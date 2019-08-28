class TodoList {
	constructor() {
		this.todos = [];
	}

	add(todo){
		this.todos.push({text: todo, completed: false})
	}

	find(text){
		return this.todos.find(todo => todo.text === text)
	}

	remove(text){
		let todo = this.find(text)
		let idx = this.todos.indexOf(todo)
		this.todos.splice(idx, 1)
	}

	toggleComplete(todo){
		let idx = this.todos.indexOf(todo)
		this.todos[idx].completed = !this.todos[idx].completed
	}
}

let todolist = new TodoList()

const inBtn = document.querySelector('#btn-add')
const todoInput = document.querySelector('input[name="todoInput"')
const listholder = document.querySelector('.list-holder')

inBtn.addEventListener('click', ()=>{
	todolist.add(todoNew.value)
})


//event listeners
function addTodo(){
	if (todoInput.value) {
		todolist.add(todoInput.value)
		let todoElement = document.createElement('li')
		let deleteBtn = document.createElement('i')
		let toggleBtn = document.createElement('i')
		todoElement.innerText = todoInput.value
		deleteBtn.classList.add('fas')
		deleteBtn.classList.add('fa-times')
		toggleBtn.classList.add('fas')
		toggleBtn.classList.add('fa-check')
		todoElement.appendChild(deleteBtn)
		todoElement.appendChild(toggleBtn)
		listholder.appendChild(todoElement)
		todoInput.value = ''
	}
}


todoInput.addEventListener('keydown', (evt)=>{
	if (evt.key === 'Enter') {
		addTodo();
	}
})