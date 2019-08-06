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

