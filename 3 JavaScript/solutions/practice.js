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
