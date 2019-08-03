// script.js

// let alpha = 'abcdefghijklmnopqrstuvwxyz'.split('');

// function encode(text, rotation=13) {

// 	let cypher = '';
// 	for (letter of text) {
// 		cypher.push(alpha[letter + rotation])
// 	}
// 	return cypher
// }
// console.log(encode('abc'))




function rot13(str) { // LBH QVQ VG!
 return str.split('')
  // Iterate over each character in the array
    .map.call(str, function(char) {
      // Convert char to a character code
     let x = char.charCodeAt(0);
      // Checks if character lies between A-Z
      if (x < 65 || x > 90) {
        return String.fromCharCode(x);  // Return un-converted character
      }
      //N = ASCII 78, if the character code is less than 78, shift forward 13 places
      else if (x < 78) {
        return String.fromCharCode(x + 13);
      }
      // Otherwise shift the character 13 places backward
      return String.fromCharCode(x - 13);
    }).join(''); 
}

console.log(rot13('I LOVE PIZZA'));
