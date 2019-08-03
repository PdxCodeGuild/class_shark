
function convertToMeter(distance, units) {
	let converter = {
		'feet': 0.3048,
		'miles': 1609.34,
		'yards': 0.9144,
		'inches': 0.0254,
		'kilometers': 1000,
		'meters': 1,
	}
	return (distance * converter[units])
}


function convertFromMeter(distance, units) {
	let converter = {
		'feet': 0.3048,
		'miles': 1609.34,
		'yards': 0.9144,
		'inches': 0.0254,
		'kilometers': 1000,
		'meters': 1,
	}

	return distance / converter[units]
}


console.log(convertToMeter(10, 'feet'))

console.log(convertFromMeter(10, 'feet'))