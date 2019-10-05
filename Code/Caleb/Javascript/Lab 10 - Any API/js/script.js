function getRandomFoxPic() {
    fetch('https://cors-anywhere.herokuapp.com/https://randomfox.ca/floof/')
    .then(res => res.json())
    .then(jsonRes => {
        console.log(jsonRes)
        console.log('break')
        var pic_url = jsonRes['image']
        document.getElementById('randFoxPic').src = pic_url
    })
    .catch(err => console.log(err))
}

const myButton = document.getElementById('btn');
myButton.onclick = function() {
    getRandomFoxPic();
}

