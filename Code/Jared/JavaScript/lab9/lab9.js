const vm = new Vue({
	el: '#container',

	data:{
		message: 'Random Quote Generator',
		quote: null,
		author: null,

	},
	methods: {
		
		getQuote: async function(){
			const endpoint = 'https://cors-anywhere.herokuapp.com/https://favqs.com/api/qotd'
			// const config = {
			// 	params: {
			// 		// id: 'id',
			// 		author: 'author',
			// 		body: 'body',
			// 	}
			// }
			const response = await axios.get(endpoint)
			// const data = response.data

		this.quote = response.data.quote.body
		this.author = response.data.quote.author


		},


	},

	mounted(){
		this.getQuote()
	},

})