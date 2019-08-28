
const language = 'en'
const word_id = 'sad'
const endpoint = 'entries'
const url = 'https://cors-anywhere.herokuapp.com/https://od-api.oxforddictionaries.com:443/api/v2/' + endpoint + '/'  + language + '/'  + word_id


const vm = new Vue({
	el: '#container',
	delimiters: ['${', '}'],

	data:{
		message: 'Oxford English Dictionary API',
		word: null,
		API_KEYS: null,
	},
	methods:{
		getApiKeys: async function() {
			const res = await axios.get('api_keys')
			console.log(res)
			this.API_KEYS = res.data
			this.getWord()
		},
		getWord: async function(){
			const contigent={
				headers: {
					app_id: this.API_KEYS.app_id,
					app_key: this.API_KEYS.app_key, 
				}
			}
			const response = await axios.get(url, contigent)
			this.word = response
		},
	},
	mounted(){

		this.getApiKeys()
		// this.getWord()
	}
})	