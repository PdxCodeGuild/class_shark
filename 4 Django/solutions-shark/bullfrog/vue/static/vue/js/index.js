// single page vue blog app
// set API endpoint
const api_root = 'api/blogposts/'

// configure axios to add CSRF token to header
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"


const app = new Vue({
    el: '#app',
    delimiters: ['${', '}'],
    data: {
        blogposts: [],
        blogpost: {
            title: null,
            text: null,
        },
        adding: false,
        editing: false,
    },
    methods: {
        getBlogposts: async function() {
            try {
                const res = await axios.get(api_root)
                this.blogposts = res.data
            } catch (err) {
                console.log(err)
            }
        },
        addBlogpost: async function() {
            try {
                const res = await axios.post(api_root, {
                    title: this.blogpost.title, 
                    text: this.blogpost.text, 
                    published_date: new Date()
                })
                console.log(res)
                this.blogpost = {title: null, text: null}
                this.adding = false
                this.getBlogposts()
            } catch (err) {
                console.log(err)
            }            
        },
        isEditing(blogpost) {
            this.editing = true
            this.blogpost = blogpost
        },
        editBlogpost: async function() {
            this.blogpost.published_date = new Date()
            try {
                const res = await axios.put(this.blogpost.url, this.blogpost)
                console.log(res)
                this.blogpost = {title: null, text: null}
                this.editing = false
                this.getBlogposts()
            } catch (err) {
                console.log(err)
            }                        
        },
        deleteBlogpost: async function(blogpost) {
            try {
                const res = await axios.delete(blogpost.url)
                console.log(res)
                this.getBlogposts()
            } catch (err) {
                console.log(err)
            }                        
        },
    },
    mounted() {
        this.getBlogposts()
    }
})