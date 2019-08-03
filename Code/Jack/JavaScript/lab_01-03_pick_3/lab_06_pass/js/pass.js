/******************************************************************/

// $('#myForm').submit(function() {
//     // Get all the forms elements and their values in one step
//     var values = $(this).serialize();

// });

/******************************************************************/


function grabInput() {
	var	numOfLoLet = document.getElementById("numOfLoLet").value;
	var numOfUpLet = document.getElementById("numOfUpLet").value;
	var	numOfNum = document.getElementById("numOfNum").value;
	var numOfPunc = document.getElementById("numOfPunc").value;
}

function constructPass() {
	var lowerLetters = "abcdefghijklmnopqrstuvwxyz"
	var upperLetters = lowerLetters.toUpperCase()
	var puncuation = "!@#$%^&*()_+{}:<>?-=[];',./|`~'"
	var numbers = "0123456789"
	var	numOfLoLet = document.getElementById("numOfLoLet").value;
	var numOfUpLet = document.getElementById("numOfUpLet").value;
	var	numOfNum = document.getElementById("numOfNum").value;
	var numOfPunc = document.getElementById("numOfPunc").value;
	var password = ''
	var temp = 0
	for (let i = 0; i < numOfLoLet; i++) {
		var rand = Math.random();
		temp = numOfLoLet
		rand *= lowerLetters.length;
		rand = Math.floor(rand);
		password += lowerLetters[rand];
	}
	for (let i = 0; i < numOfUpLet; i++) {
		var rand = Math.random();
		temp = numOfUpLet
		rand *= upperLetters.length;
		rand = Math.floor(rand);
		password += upperLetters[rand];
	}
	for (let i = 0; i < numOfNum; i++) {
		var rand = Math.random();
		temp = numOfNum
		rand *= numbers.length;
		rand = Math.floor(rand);
		password += numbers[rand];
	}
	for (let i = 0; i < numOfPunc; i++) {
		var rand = Math.random();
		temp = numOfPunc
		rand *= puncuation.length;
		rand = Math.floor(rand);
		password += puncuation[rand];
	}
	var shuffled = shuffelWord(password)
	return shuffled
}


function shuffelWord (word){
    var shuffledWord = '';
    pWord = word.split('');
    while (pWord.length > 0) {
      shuffledWord +=  pWord.splice(pWord.length * Math.random() << 0, 1);
    }
    return shuffledWord;
}


const myButton = document.getElementById('btnOne');
myButton.onclick = function() {
	outPass = constructPass();
	document.getElementById('showPass').innerText = 'Password: ' + outPass
}
