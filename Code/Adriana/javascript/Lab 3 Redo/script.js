function LetterGrade() {
    var grade = document.getElementById('grade').value;
    var result = document.getElementById('output');

    if( grade >= 90 && grade <= 100) {
       result.innerHTML = "You got an 'A'. Awesome!"
    }
    else if ( grade >= 80 && grade < 90) {
        result.innerHTML = "You got an 'B'. Nice!"
    }
    else if ( grade >= 70 && grade < 80) {
        result.innerHTML = "You got an 'C'. Room for improvement!"
    }
    else if ( grade >= 60 && grade < 70) {
        result.innerHTML = "You got an 'D'. Do better, work harder"
    }
    else if ( grade < 60) {
        result.innerHTML = "You got an 'F'. Get a tutor"
    }
    else{
        window.alert("Invalid grade. Please enter a number grade.")
    }
    }
