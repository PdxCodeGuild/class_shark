/******************************************************************/

// $('#myForm').submit(function() {
//     // Get all the forms elements and their values in one step
//     var values = $(this).serialize();

// });

/******************************************************************/


function grabInput() {
	var A_Place = document.getElementById("aPlace").value
	var	Adjective_1 = document.getElementById("adjOne").value
}

const myButton = document.getElementById('btnOne');
myButton.onclick = function() {
	grabInput();
}