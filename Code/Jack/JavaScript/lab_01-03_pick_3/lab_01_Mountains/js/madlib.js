/*Albert Einstein, the son of 5.and 4,

was born in Ulm, Germany, in 1879. In 1902, he had a job

as assistant 6.in the Swiss patent office and attended

the University of Zurich. There he began studying atoms, molecules,

and 9. He developed the theory of

2.relativity, which expanded the phenomena of sub-atomic

10.and 3.magnetism. In 1921,

he won the Nobel prize for 11.and was director of

theoretical physics at the Kaiser Wilhelm 7.in Berlin.

In 1933, when Hitler became Chancellor of 1,

Einstein came to America to take a post at Princeton Institute for

12, where his theories helped America devise the first

atomic 8. There is no question about it: Einstein was

one of the most brilliant 13.of our time.*/

/******************************************************************/

// $('#myForm').submit(function() {
//     // Get all the forms elements and their values in one step
//     var values = $(this).serialize();

// });

/******************************************************************/


function grabInput() {
	var A_Place = document.getElementById("aPlace").value
	var	Adjective_1 = document.getElementById("adjOne").value
	var	Adjective_2 = document.getElementById("adjTwo").value
	var	Female_Celebrity = document.getElementById("fCeleb").value
	var	Male_Celebrity = document.getElementById("mCeleb").value
	var	Noun_1 = document.getElementById("nounOne").value
	var	Noun_2 = document.getElementById("nounTwo").value
	var	Noun_3 = document.getElementById("nounThree").value
	var	Plural_Noun_1 = document.getElementById("pNounOne").value
	var	Plural_Noun_2 = document.getElementById("pNounTwo").value
	var	Plural_Noun_3 = document.getElementById("pNounThree").value
	var	Plural_Noun_4 = document.getElementById("pNounFour").value
	var	Plural_Profession = document.getElementById("pProfession").value
	alert('Albert Einstein, the son of ' + Male_Celebrity + ' and ' + Female_Celebrity + 
		', was born in Ulm, Germany, in 1879. In 1902, he had a job' +

' as assistant ' + Noun_1 + ' in the Swiss patent office and attended' +

'the University of Zurich. There he began studying atoms, molecules,'+

'and ' + Plural_Noun_1 + ' He developed the theory of' +

 Adjective_1 + ' relativity, which expanded the phenomena of sub-atomic' +
Plural_Noun_2 + ' and ' + Adjective_2 + ' magnetism. In 1921,' +

'he won the Nobel prize for ' + Plural_Noun_3 + ' and was director of'+

'theoretical physics at the Kaiser Wilhelm ' + Noun_2 + ' in Berlin.'+

'In 1933, when Hitler became Chancellor of ' + A_Place + ','+

'Einstein came to America to take a post at Princeton Institute for'+

 Plural_Noun_4 + ' where his theories helped America devise the first'+

'atomic ' + Noun_3 + ' There is no question about it: Einstein was'+

'one of the most brilliant ' + Plural_Profession + ' of our time.');

}

const myButton = document.getElementById('btnOne');
myButton.onclick = function() {
	grabInput();
}