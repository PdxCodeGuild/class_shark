/* Basic Algorithm Scripting: Find the Longest Word in a String
Return the length of the longest word in the provided sentence. */

// looping through index
function findLongestWordLength(str) {
  // split str into word list
  let words = str.split(' ')
  // set longest to 0
  let longest = 0
  // loop through words
  for (let i=0; i<words.length; i++) {
    // if current word > longest 
    if (words[i].length > longest) {
      // then longest = current word
      longest = words[i].length
    }
  }
  // return longest
  return longest
}

// looping with for..of (looping through words directly)
function findLongestWordLength(str) {
  let words = str.split(' ')
  let longest = 0
  for (let word of words) {
    if (word.length > longest) longest = word.length
  }
  return longest 
}

// looping with forEach
function findLongestWordLength(str) {
  let words = str.split(' ')
  let longest = 0
  words.forEach(function(word) {
    longest = (word.length > longest ? word.length : longest)
  })
  return longest 
}

// reduce solution
function findLongestWordLength(str) {
  let words = str.split(' ')
  let longest = words.reduce(
    (acc, cur) => (cur.length > acc.length ? cur : acc)
  )
  return longest.length
}


/* Basic Algorithm Scripting: Confirm the Ending
Check if a string (first argument, str) ends with the given target string (second argument, target). */

// built-in solution
function confirmEnding(str, target) {
  return str.endsWith(target);
}

// slice solution (compare substrings)
function confirmEnding(str, target) {
  return str.slice(-target.length) === target;
}

/* Basic Algorithm Scripting: Falsy Bouncer
Filter out all falsy values from an array.

Falsy values in JavaScript are false, null, 0, "", undefined, and NaN. */

function bouncer(arr) {
  return arr.filter(elem => elem)
}

// equivalent to above
function bouncer(arr) {
  let truthy = []
  for (let elem of arr) {
    if (elem) truthy.push(elem)
  }  
  return truthy
}

function bouncer(arr) {
  return arr.filter(Boolean)
}


/* Basic Algorithm Scripting: Slice and Splice
You are given two arrays and an index.
Use the array methods slice() and splice() to copy each element of the first array into the second array, in order.
Begin inserting elements at index n of the second array.
Return the resulting array. The input arrays should remain the same after the function runs. */

function frankenSplice(arr1, arr2, n) {
  let ret = arr2.slice()      // copy of arr2
  ret.splice(n, 0, ...arr1);  // at index n, remove 0 elements,
                              // and insert all the elements of arr1
  return ret
}


/* Basic Algorithm Scripting: Chunky Monkey
Write a function that splits an array (first argument) into 
groups the length of size (second argument) 
and returns them as a two-dimensional array.
*/
function chunkArrayInGroups(arr, size) {
  let chunks = []
  for (let i=0; i<arr.length; i+=size) {
    chunks.push(arr.slice(i, i+size))
  }
  return chunks  
}

/* Basic Algorithm Scripting: Title Case a Sentence
Return the provided string with the first letter of each word capitalized. 
Make sure the rest of the word is in lower case.
*/

// using map
function titleCase(str) {
  return str.split(' ')
            .map(word => word[0].toUpperCase() + word.slice(1).toLowerCase())
            .join(' ')
}

// old fashioned loop
function titleCase(str) {
    // convert str into array of words
    let words = str.split(' ')
    // loop through words
    for (let i=0; i<words.length; i++) {
        let word = ''
    // set first char uppercase
        word += words[i][0].toUpperCase()
    // set rest of word lowercase
        word += words[i].slice(1).toLowerCase()
        words[i] = word
    }
    // join array of words back into string
    return words.join(' ')
}

// using reduce
function titleCase(str) {
    return str.split(' ')
              .reduce((acc, word) => acc +' '+ word[0].toUpperCase() + word.slice(1).toLowerCase(), '')
              .trim()
}

/* Practice: Sum All Numbers in a Range
We'll pass you an array of two numbers. 
Return the sum of those two numbers plus the sum of all the numbers between them.
The lowest number will not always come first.

sumAll([1, 4]) // returns 10 (because 1+2+3+4)
sumAll([10, 5]) */
function sumAll(arr) {
  // sort arr
  const [a, b] = arr.sort((a, b) => a-b)
  // get range from a to b
  const range = []
  for (let i=a; i<=b; i++) {
    range.push(i)
  }
  // // alternately, single line range
  // const range = Array.from(Array(b-a+1).keys(), num => num + a)
  // sum all elements in range
  return range.reduce((acc, cur) => acc + cur)
}

/* Intermediate Algorithm Scripting: Convert HTML Entities
Convert the characters &, <, >, " (double quote), and ' (apostrophe), 
in a string to their corresponding HTML entities. */
function convertHTML(str) {
  // &colon;&rpar;
  const html = {
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      '"': '&quot;',
      "'": '&apos;',
  }
  let chars = str.split('')
  console.log(chars)
  for (let i=0; i<chars.length; ++i) {
      if (chars[i] in html) {
          chars[i] = html[chars[i]]
      }
  }
  console.log(chars)
  return chars.join('');
}

// map solution
function convertHTML(str) {
  const html = {
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      '"': '&quot;',
      "'": '&apos;',
  }
  let chars = str.split('')
  chars = chars.map(letter => ((letter in html) ? html[letter] : letter))
  // [html.get(letter, letter) for letter in chars]
  return chars.join('')
}

// reduce solution
function convertHTML(str) {
  const html = {
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      '"': '&quot;',
      "'": '&apos;',
  }
  let chars = str.split('')
  chars = chars.reduce((acc, letter) => acc + ((letter in html) ? html[letter] : letter), '')
  console.log(chars)
  return chars
}

// switch case solution
function convertHTML(str) {
    let chars = str.split('')
    let ret = ''
    for (let char of chars) {
        switch(char) {
            case '&':
                ret += '&amp;'
                break
            case '<':
                ret += '&lt;'
                break
            case '>':
                ret += '&gt;'
                break
            case '"':
                ret += '&quot;'
                break        
            case "'":
                ret += '&apos;'
                break
            default:
                ret += char                           
        }
    }
    return ret
}

