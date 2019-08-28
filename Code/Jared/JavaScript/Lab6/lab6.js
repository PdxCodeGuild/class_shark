function clock(){
	// function to create date and turn into readable string
	var day = new Date();
	document.querySelector('#clock').innerHTML = day.toLocaleTimeString()
}

function stopwatch(){
	var start = Date.now()

	var stop = Date.now()


}

// set interval to show current time
let time = setInterval(clock, 1000)