var app = new Vue({
    el: '#app',
    data: {
        message: 'todos:',
        todos: [
            {todo: 'Learn Vue.js', completed: false},
            {todo: 'Master frontend', completed: false}
        ],
        todo: '',
    },
    methods: {
        addTodo: function() {
            // add todo to this.todos
            this.todos.push({todo: this.todo, completed: false})
        },
        removeTodo: function(index) {
            // remove todo from this.todos
        },
        markDone: function(index) {
            // mark todo as done
        },
    },
});
