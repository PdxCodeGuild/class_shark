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


function theFunc(ele) {
	var here = ele.id;
	var string = `#${here}`;
	alert(string);
	var temp = document.querySelector(id='#btnOne');
	var color = 'blue';
	document.querySelector(id='#btnOne').style.backgroundColor = color;
}

const btn = document.querySelector('#btnOne')
btn.addEventListener('click', theFunc(this))