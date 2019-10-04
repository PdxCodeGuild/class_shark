new Vue({
    el: '#vue-app',
    data: {
        name:'Caleb',
        job:'Woodworker',
        website:'http://www.thenetninja.co.uk',
        websiteTag: '<a href="http://thenetninja.co.uk">The Net Ninja Website</a>',
        age:28,
        x:0,
        y:0,
    },
    methods:{
        greet: function(time){
            return 'Good' + time + ' ' + this.name;
        },
        add: function(inc){
            this.age += inc;
        },
        subtract: function(dec){
            this.age -= dec;
        },
        updateXY: function(event){
            this.x = event.offsetX;
            this.y = event.offsetY;
        },
        click: function(){
            alert('You clicked me');
        },
        logName: function(){
            console.log('You entered your name');
        },
        logAge: function(){
            console.log('You entered your age');
        }
    }
});
