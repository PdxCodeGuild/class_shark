axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

const app = new Vue({
    el: '#app',
    delimiters: ['${', '}'], // set custom delimiters here instead of {{}}    
    data: {
        todos: [],
        todo: '',
        owner: '',
    },
    methods: {
        grabTodos: async function() {
            const response = await axios.get('api/todos/')
            this.todos = response.data 
            this.owner = this.todos[0].owner
        },
        addTodo: async function() {
            const response = await axios.post('api/todos/', {text: this.todo})
            console.log(response)
            this.grabTodos()
            // // add todo to this.todos
            // this.todos.push({text: this.todo, completed: false})
            this.todo = ''
        },
        removeTodo: async function(index) {
            const response = await axios.delete(`/api/todos/${this.todos[index].pk}/`)
            console.log(response)            
            // remove todo from this.todos
            // this.todos.splice(index, 1)
            this.grabTodos()
        },
        toggleComplete: async function(index) {
            const todo = this.todos[index]
            todo.completed = !todo.completed
            const fields = {
                completed: todo.completed,
                completed_date: (todo.completed ? new Date() : null)
            }
            const response = await axios.patch(`/api/todos/${todo.pk}/`, fields)
            // // mark todo as done
            // this.todos[index].completed = !this.todos[index].completed            
            this.grabTodos()
        },
    },
    mounted: function() {
        // mounted() handles any logic you want prior to the vue app mounting
        // this is a good place to request any data you want to render, such as from localStorage (what we're doing here), or from an API call
        this.grabTodos()
    },
    computed: {
        message: function() {
            return `${this.owner}'s todo list:`
        },
        count: function() {
            return this.todos.length
        }
    },
});
