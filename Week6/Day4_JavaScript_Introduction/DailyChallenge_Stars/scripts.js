// Instructions
// Write a JavaScript program that recreates the pattern below.
// Do this challenge twice: first by using one loop, then by using two nested for loops(Nested means one inside the other - check out this tutorial of nested loops).
// Do this Daily Challenge by yourself, without looking at the answers on the internet.
// *  
// * *  
// * * *  
// * * * *  
// * * * * *
// * * * * * *


// With one loop

let rows = 6
let star = ''

for (let i = 0; i < rows; i++) {
    star += ' * '
    document.write(star + '<br />')
}


// With nested loops

for (let i = 1; i <= rows; i++) {
    for (let j = 1; j <= i; j++) {
        document.write(' * ');
    }
    document.write('<br />');
}