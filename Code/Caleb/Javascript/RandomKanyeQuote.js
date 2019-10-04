async function getRandomYeezyQuote() { // Step 1
    const res = await fetch('https://api.kanye.rest/'); // Step 2
    const jsonRes = await res.json(); // Step 2

    console.log(jsonRes); // Step 3
}

getRandomYeezyQuote();