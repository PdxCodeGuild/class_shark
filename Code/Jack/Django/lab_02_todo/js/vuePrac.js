var app = new Vue({
  el: '#app',
  data: {
    message: 'Todos:',
    todos: [
	  {todo: 'Learn Vue.js', completed: false},
	  {todo: 'Master Vue.js', completed: false}
	],
	todo: '',
  }	,
  methods: {
    addTodo: function() {
        // add todo to the front of this.todos
        this.todos.push({todo: this.todo, completed: false})
        this.todo = ''

    },

    removeTodo: function(index) {
        // remove todo from this.todos
        this.todos.splice(index, 1)
    },
    
    markDone: function(index) {
        // toggle todo.completed
        // if completed: move todo to the front of todos
        // else: move todo to the end of todos
        this.todos[index].completed = !this.todos[index].completed
    }
  }

})