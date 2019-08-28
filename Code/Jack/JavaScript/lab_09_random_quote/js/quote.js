let app = new Vue({
  el: '#quote',
  data: {
    returns: {},
    message: '',
    author: '',
  },
  methods: {
    get: async function() {
      this.returns = await axios.get('https://favqs.com/api/qotd');
      console.log(this.returns)
      this.message = '"' + this.returns["data"]["quote"]["body"] + '"'
      this.author = '-' + this.returns["data"]["quote"]["author"]
      this.link = this.returns["data"]["quote"]["url"]

    },


  },

  mounted: function() {
    this.get()
  }
})
