let PuppyChowApp = new Vue({
  el: '#puppyChow',
  data: {
    api: 'http://www.recipepuppy.com/api/'
    resp: {},
    author: '',
  },
  methods: {
    get: async function() {
      let gotten = this.api + this.ingr.join(',').toLowerCase()
      this.resp = await axios.get(gotten);
      console.log(this.resp)
      // this.message = '"' + this.returns["data"]["quote"]["body"] + '"'
      // this.author = '-' + this.returns["data"]["quote"]["author"]
      // this.link = this.returns["data"]["quote"]["url"]

    },


  },

  mounted: function() {
    this.get()
  }
})
