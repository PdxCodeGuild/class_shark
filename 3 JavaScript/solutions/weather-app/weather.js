// weather.js

const app = new Vue({
  el: '#weather-app',
  data: {
    location: null,
    zip: null,
    lat: null,
    lon: null,
    weather: null,
    description: null,
    icon: null,
    hi: null,
    lo: null,
    temp: null,
    catFact: null
  }, 
  methods: {
    getWeatherData: async function() {
      const endpoint = 'http://api.openweathermap.org/data/2.5/weather'
      let config
      if (this.zip) {
        config = {
          params: {
            appid: '847b317dd0b65a4de6755ad19098a2c1',
            zip: this.zip,
            units: 'imperial'
          }
        }            
      } else {
        config = {
          params: {
            appid: '847b317dd0b65a4de6755ad19098a2c1',
            lat: this.lat,
            lon: this.lon,
            units: 'imperial'
          }
        }  
      }
      const response = await axios.get(endpoint, config)
      const data = response.data
      const weather = data.weather[0]
      console.log(response.data)
      this.location = data.name
      this.weather = weather.main
      this.description = weather.description
      this.icon = `http://openweathermap.org/img/wn/${weather.icon}.png`
      this.hi = data.main.temp_max
      this.lo = data.main.temp_min
      this.temp = data.main.temp
    },
    getLocation: function() {
      navigator.geolocation.getCurrentPosition(position => {
        this.lat = position.coords.latitude
        this.lon = position.coords.longitude
        localStorage.setItem('lat', this.lat)
        localStorage.setItem('lon', this.lon)
        this.getWeatherData()
      })
    },
    getCatFact: async function() {
      const endpoint = 'https://cors-anywhere.herokuapp.com/https://cat-fact.herokuapp.com/facts/random'
      const config = {
        params: {
          animal_type: 'cat',
          amount: 1
        }
      }
      const response = await axios.get(endpoint, config)
      this.catFact = response.data.text
    }
  },
  mounted() {
    const lat = localStorage.getItem('lat')
    const lon = localStorage.getItem('lon')
    if (lat && lon) {
      this.lat = lat 
      this.lon = lon
      this.getWeatherData()
    } else {
      this.getLocation()
    }
    this.getCatFact()
  }
})