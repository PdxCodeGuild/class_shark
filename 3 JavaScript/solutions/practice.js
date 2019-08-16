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


/* Intermediate Algorithm Scripting: Pig Latin
Translate the provided string to pig latin.
Pig Latin takes the first consonant (or consonant cluster) of an English word, 
moves it to the end of the word and suffixes an "ay".
If a word begins with a vowel you just add "way" to the end. */
function translatePigLatin(str) {
  const vowels = 'aeiou'
  // word starts with a vowel end with 'way'
  if (vowels.includes(str[0])) return str+'way'
  // word starts with a consonant
  for (let i=1; i<str.length; i++) {
    // loop through until we encounter a vowel
    if (vowels.includes(str[i])) {
      // move the consonants to the end of the word and add 'ay'
      return str.slice(i) + str.slice(0, i) + 'ay'
    }
  }
  // word that has no vowels
  return str + 'ay'
}

translatePigLatin("consonant");

/* Intermediate Algorithm Scripting: Diff Two Arrays
Compare two arrays and return a new array with any items only found in 
one of the two given arrays, but not both. 
In other words, return the symmetric difference, or XOR of the two arrays. */

// loop solution
function diffArray(arr1, arr2) {
  // combine arrays
  let union = [...arr1, ...arr2]
  let xor = []
  // loop through each item
  for (let elem of union) {
    // grab item if it is in arr1 or arr2 but not both
    if (!(arr1.includes(elem) && arr2.includes(elem))) {
      xor.push(elem)
    }
  }
  return xor
}

// filter solution
function diffArray(arr1, arr2) {
  // combine arrays
  let union = [...arr1, ...arr2]
  // loop through each item
  return union.filter(elem => !(arr1.includes(elem) && arr2.includes(elem)))
}

// set solution
function diffArray(arr1, arr2) {
  const set1 = new Set(arr1)
  const set2 = new Set(arr2)
  const union = new Set([...set1, ...set2])
  return [...union].filter((elem) => !(set1.has(elem) && set2.has(elem)))
}

/* Intermediate Algorithm Scripting: Spinal Tap Case
Convert a string to spinal case. Spinal case is all-lowercase-words-joined-by-dashes.
*/
function spinalCase(str) {
  // "It's such a fine line between stupid, and clever."
  // --David St. Hubbins
  const sep = /[\s_-]/g
  const camel = /([a-z])([A-Z])/g
  str = str.replace(camel, '$1-$2')
  str = str.replace(sep, '-')
  return str.toLowerCase()
}

/* Intermediate Algorithm Scripting: Search and Replace
Perform a search and replace on the sentence using the arguments provided and return the new sentence.
First argument is the sentence to perform the search and replace on.
Second argument is the word that you will be replacing (before).
Third argument is what you will be replacing the second argument with (after).

Note:
Preserve the case of the first character in the original word when you are replacing it. 
For example if you mean to replace the word "Book" with the word "dog", 
it should be replaced as "Dog" */

function myReplace(str, before, after) {
  // if before is capitalized
  // get after to have the same casing as before
  if (before[0].toUpperCase() === before[0]) { 
    after = after[0].toUpperCase() + after.slice(1)
  } else {
    after = after[0].toLowerCase() + after.slice(1)
  }
  return str.replace(before, after);
}

/* ntermediate Algorithm Scripting: Drop it
Given the array arr, iterate through and remove each element starting from the first element 
(the 0 index) until the function func returns true when the iterated element is passed through it.
Then return the rest of the array once the condition is satisfied, 
otherwise, arr should be returned as an empty array. */
function dropElements(arr, func) {
  for (let i=0; i<arr.length; i++) {
    if (func(arr[i])) return arr.slice(i)      
  }
  return []
}

function dropElements(arr, func) {
  // loop through arr indexes
  while (!func(arr[0])) {
    arr.shift()
  }
  return arr
}

function dropElements(arr, func) {
  // loop through arr indexes
  let firstTrue = false
  return arr.reduce((acc, cur) => {
    if (firstTrue || func(cur)) {
      firstTrue = true
      return [...acc, cur]
    } else {
      return []
    }
  }, [])
}

function dropElements(arr, func) {
  // loop through arr indexes
  let firstTrue = false
  return arr.filter((cur) => {
    if (firstTrue || func(cur)) {
      firstTrue = true
      return true
    } else {
      return false
    }
  })
}

