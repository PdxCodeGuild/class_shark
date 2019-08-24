//make change lab into JS

//LAB 08 Make Change
//Step 1 Convert a dollar amount into a number of coins.
//Step 2 Output will be total number of quarters, dimes, nickles



let total_amt = parseInt(prompt('How many pennies?: '))

var quarters, dimes, nickles;

quarters = total_amt / 25
total_amt -= quarters*25

dimes = total_amt / 10
total_amt -= dimes*10

nickles = total_amt / 5
total_amt -= nickles*5


window.alert(quarters + 'quarters' + dimes + 'dimes' + nickles + 'nickles' + total_amt + 'pennies')
