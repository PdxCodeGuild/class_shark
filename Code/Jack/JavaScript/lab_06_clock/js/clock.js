let app = new Vue({
  el: '#clockApp',
  data: {
    clockTime: 'this here',
    interval: null,
    stopwatch: 'stop watch',
    timer: 'timer',
  },
  methods: {
    getTime: function() {
      var date = new Date();
      var h = date.getHours(); // 0 - 23
      var m = date.getMinutes(); // 0 - 59
      var s = date.getSeconds(); // 0 - 59
      var session = "AM";
      
      if(h == 0){
          h = 12;
      }
      
      if(h > 12){
          h = h - 12;
          session = "PM";
      }
      
      h = (h < 10) ? "0" + h : h;
      m = (m < 10) ? "0" + m : m;
      s = (s < 10) ? "0" + s : s;
      
      this.clockTime = (h + ":" + m + ":" + s + " " + session);
    },
  },

  mounted: function() {
    this.interval = setInterval(this.getTime, 1000)
  }
})