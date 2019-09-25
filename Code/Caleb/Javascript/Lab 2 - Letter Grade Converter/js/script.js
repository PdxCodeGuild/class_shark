function convertGrade() {
    var score = document.getElementById("score").value
    if (score >= 98) {
        alert('The score converts to a grade of A+');
    } else if (score >= 92) {
        alert('The score converts to a grade of A');
    } else if (score >= 90) {
        alert('The score converts to a grade of A-');
    } else if (score >= 88) {
        alert('The score converts to a grade of B+');
    } else if (score >= 82) {
        alert('The score converts to a grade of B');
    } else if (score >= 80) {
        alert('The score converts to a grade of B-');
    } else if (score >= 78) {
        alert('The score converts to a grade of C+');
    } else if (score >= 72) {
        alert('The score converts to a grade of C');
    } else if (score >= 70) {
        alert('The score converts to a grade of C-');
    } else if (score >= 60) {
        alert('The score converts to a grade of D');
    } else if (score >= 50) {
        alert('The score converts to a grade of F');
    }    
}


const myButton = document.getElementById('btn');
myButton.onclick = function() {
    convertGrade();
}

// # Figure out if the grade is a '+' or '-'
// # If the number 100 or greater, add the suffix '+', as that is an A+ grade.

