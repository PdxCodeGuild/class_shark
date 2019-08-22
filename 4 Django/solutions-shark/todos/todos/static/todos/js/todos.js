var app = new Vue({
    el: '#app',
    delimiters: ['${', '}'], // set custom delimiters here instead of {{}}    
    data: {
        message: 'Your todo list:',
        todos: [
            {text: 'Learn Vue.js', completed: false},
            {text: 'Master frontend', completed: false}
        ],
        todo: '',
    },
    methods: {
        addTodo: function() {
            // add todo to this.todos
            this.todos.push({text: this.todo, completed: false})
            this.todo = ''
        },
        removeTodo: function(index) {
            // remove todo from this.todos
            this.todos.splice(index, 1)
        },
        toggleComplete: function(index) {
            // mark todo as done
            this.todos[index].completed = !this.todos[index].completed            
        },
    },
    mounted: function() {
        // mounted() handles any logic you want prior to the vue app mounting
        // this is a good place to request any data you want to render, such as from localStorage (what we're doing here), or from an API call
        let cachedTodos = localStorage.getItem('todos')
        if (cachedTodos) {
            cachedTodos = JSON.parse(cachedTodos)
            this.todos = cachedTodos
        }
    },
});

// store todos to localStorage before the page unloads
window.addEventListener('unload', evt => {
  let todosJSON = JSON.stringify(app.todos)
  localStorage.setItem('todos', todosJSON)
})