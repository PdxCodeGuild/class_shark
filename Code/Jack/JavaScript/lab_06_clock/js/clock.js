var countdown = new Vue({
	el: '#countdown',
	data: {
		isrc : 'index.html',
		time : 5,
		siteList: ['https://en.wikipedia.org/wiki/Steel_(1997_film)'
					,"http://www.mozilla.org"
					,'https://www.imdb.com/title/tt0062803/'
					//,'https://www.youtube.com/watch?v=xfr64zoBTAQ',
					],
	},
	methods: {
		goGoGo: function() {
			//window.location.assign(this.siteList[this.getRand(0,this.siteList.length)])
			this.isrc = this.siteList[this.getRand(0,this.siteList.length)]
			this.time = 5

		},

		getRand: function(min, max) {
			return Math.floor(Math.random() * (max - min) + min);
		},

		beginCount: function(duration, display) {
    		let myVar = setInterval(this.counting, 1000)
    	},

    	counting: function () {
			console.log('here')
    		this.time = this.time - 1
	        if (this.time <= 0) {
            	this.goGoGo();
       		}
    	},
	},
})



