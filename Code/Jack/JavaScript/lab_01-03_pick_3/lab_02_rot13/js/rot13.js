function encode(msg, ciphRot) {
	let encMsg = ''
	for (let i = 0; i < msg.length; i++) {
		if (msg[i] == msg[i].toUpperCase()) {
			encMsg += ciphUp[(ciphUp.indexOf(msg[i]) + ciphRot) % 26]
		} else if (msg[i] == msg[i].toLowerCase()) {
			encMsg += ciphLo[(ciphLo.indexOf(msg[i]) + ciphRot) % 26]
		} else {	encMsg += msg[i]	}
	}
	return encMsg
}

function decode(msg, ciphRot) {
	let decMsg = ''
	ciphRot *= -1;
	alert(ciphRot)
	for (let i = 0; i < msg.length; i++) {
		if (msg[i] == msg[i].toUpperCase()) {
			decMsg += ciphUp[(ciphUp.indexOf(msg[i]) + ciphRot) % 26]
		} else if (msg[i] == msg[i].toLowerCase()) {
			decMsg += ciphLo[(ciphLo.indexOf(msg[i]) + ciphRot) % 26]
		} else {	decMsg += msg[i]	}
	}
	return decMsg
}
////////////////////////////////////////////////
const ciphLo = 'abcdefghijklmnopqrstuvwxyz'
const ciphUp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
const rotNum = null

function timeToEncode(ele, ciphRot) {
	document.querySelector('#cipher-form').innerHTML = "Your message: <input type='text' id ='msg' placeholder='message'><br><div class='container'><a id='my-btn-dec-link'><button id='btnTwo'>Encode</button></a>"
	const msgBtn = document.querySelector('#btnTwo')
	msgBtn.addEventListener('click', (evt) => {
		evt.preventDefault();
	let msg = document.querySelector('#msg').value;
		msg = encode(msg, ciphRot);
	document.querySelector('#encMsg').innerHTML = "Your message: " + `${msg}`;
	document.querySelector('.decode-wrapper').setAttribute('style', 'visibility: visible;')
	})
	}

function timeToDecode() {
	let ugMsg = document.querySelector('#encMsg').innerHTML
	ugMsg = ugMsg.slice(14)
	alert(decode(ugMsg, rotNum))
}


///////////////////////////////////////////////

const btn = document.querySelector('#btnOne')
btn.addEventListener('click',(evt)=>{
	rotNum = document.querySelector('#rot-val').value
	rotNum = parseInt(rotNum)
	timeToEncode(this, rotNum)
})

const decBtn = document.querySelector('#decode-btn')
decBtn.addEventListener('click', (evt)=>{
	evt.preventDefault();
	timeToDecode()
})