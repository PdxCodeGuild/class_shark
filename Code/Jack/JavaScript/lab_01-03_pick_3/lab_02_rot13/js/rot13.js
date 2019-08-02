/******************************************************************/

// $('#myForm').submit(function() {
//     // Get all the forms elements and their values in one step
//     var values = $(this).serialize();

// });

/******************************************************************/


function grabInput() {
	var A_Place = document.getElementById("aPlace")
	var	Adjective_1 = document.getElementById("adjOne")
}

// const buttons = document.querySelector(".the-btn");
// buttons.forEach((button) => {
// 	button.onclick = function(B) {
// 		B.target.style.backgroundColor = "#FFFFFF";
// 		alert('HERE')
// 		B.preventDefault()
// 	}
// })

function theFunc() {
	this.style.backgroundColor = '#FFFFFF';
	alert('HERE');
}

function setUpTable(row, col) {
	const table = document.querySelector('#my-mtn-table')
	let temp = ''
	let tempCol = ''
	for (let i = 0; i < col; i++) {
		temp += `<div class='my-mtn-col'>`
		for (let j = 0; j < row; j++) {
			temp += `<button id='btn${i}${j}' onclick='theFunc()' class='the-btn'></button>`
		}
		temp += `</div>`
		tempCol += ' 1fr'

	}
	tempCol += ';'
	table.setAttribute('style', 'grid-template-columns = tempCol')

	table.innerHTML = temp
	console.log(temp)
}