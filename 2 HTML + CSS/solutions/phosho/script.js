// script.js

document.addEventListener('DOMContentLoaded', function() {
// navbar collapse logic
  var sidenavElem = document.querySelectorAll('.sidenav');
  var sidenav = M.Sidenav.init(sidenavElem, {});

// parallax logic
  var parallaxElems = document.querySelectorAll('.parallax');
  var parallax = M.Parallax.init(parallaxElems, {});

// materialize dropdown menus
  var elems = document.querySelectorAll('select');
  var instances = M.FormSelect.init(elems, {});
});

const app = new Vue({
  el: '#order-form', 
  data: {
    customer: {
      first_name: null, 
      last_name: null, 
      phone: null,
      email: null,
      address: {
        street: null,
        city: null,
        state: '', 
        zip: null
      }
    },
    order: {
      list: [],
      spicy: 'none',
      sauces: []
    }
  },
  methods: {
    post: async function(event) {
      event.preventDefault()
      const data = {customer: this.customer, order: this.order}
      try {
        const res = await axios.post('https://cors-anywhere.herokuapp.com/https://webhook.site/d5d38de0-244c-44b2-bcd4-42029a83b39f', data)
        console.log(res)
      } catch (err) {
        console.log(err)
      }
    }
  }  
})