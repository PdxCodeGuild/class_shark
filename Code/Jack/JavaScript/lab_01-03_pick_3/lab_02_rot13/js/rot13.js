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

function encode(msg) {
	let encMsg = ''
	for (let i = 0; i < msg.length; i++) {
		if (isUpperCase(msg[i])) {
			encMsg += (ciphUp.indexOf(msg[i]) + rotNum) % 26);
		} else if (isLowerCase(msg[i])) {
			encMsg += (ciphLo.indexOf(msg[i]) + rotNum) % 26);
		} else {	encMsg += msg[i]	}
	}
	return encMsg
}
////////////////////////////////////////////////

const rotNum = querySelector('#rot-val').value
rotNum = parseInt(rotNum)
const ciphLo = 'abcdefghijklmnopqrstuvwxyz'
const ciphUp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';


function timeToEncode(ele) {
document.querySelector('#cipher-form').innerHTML = "Your message: <input type='text' id ='msg' placeholder='message'><br><div class='container'><div class='my-btn-dec'><button id='btnTwo'>Encode</button>"
let msg = document.querySelector('#msg').value
const msgBtn = document.querySelector('#btnTwo')
msgBtn.addEventListener('click', (evt) => {
	msg = encode(msg);
document.querySelector('#encMsg').innerHTML = "Your message: " + `${msg}`
})
}


///////////////////////////////////////////////

const btn = document.querySelector('#btnOne')
btn.addEventListener('click', timeToEncode(this))