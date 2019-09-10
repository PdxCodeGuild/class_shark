let PuppyChowApp = new Vue({
  el: '#puppyChow',
  data: {
    api: 'https://cors-anywhere.herokuapp.com/http://www.recipepuppy.com/api/',
    ingr: '',
    ingrs: [],
    recipe: '',
    recipe_link: '',

  },
  methods: {
    get: async function() {
  
      const config =  {
        params: {
          i: this.ingrs.join(',').toLowerCase()
        }
      }
      let resp = await axios.get(this.api, config)
      this.recipe = resp.data.results[0]['title']
      this.recipe_link = resp.data.results[0]['href']
      console.log(resp)

    },

    add: function() {
      console.log(this.ingr)
      this.ingrs.push(this.ingr)
      this.ingr = ''
    },

    clear: function() {
      this.ingrs = []
      this.ingr = ''
    }

  },
})