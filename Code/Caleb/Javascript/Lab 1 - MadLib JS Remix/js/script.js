function getInput() {
    var location = document.getElementById("Location").value
    var famousPerson = document.getElementById("Famous Person").value
    var adjective = document.getElementById("Adjective").value
    var sound = document.getElementById("Sound").value
    var animalA = document.getElementById("Animal A").value
    var animalB = document.getElementById("Animal B").value
    var verb = document.getElementById("Verb").value
    alert('Just waking up in the ' + location + ', gotta thank ' + famousPerson + '. I don\'t know, but today seems kinda ' + adjective + '. No ' + sound + ' from the ' + animalA + ', no smog, and momma cooked a breakfast with no ' + animalB + '. I got my grub on, but I didn\'t pig out. Finally got a call from a girl I want to ' + verb + '. I can\'t believe today was a ' + adjective + ' day.');
}

const myButton = document.getElementById('btn');
myButton.onclick = function() {
    getInput();
}