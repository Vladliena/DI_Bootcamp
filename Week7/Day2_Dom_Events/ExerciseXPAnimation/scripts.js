/* Part I In your Javascript file,
using setTimeout,
call a function after 2 seconds. The function will alert “Hello World”. 

Part II In your Javascript file,
using setTimeout,
call a function after 2 seconds. The function will add a new paragraph <p>Hello World</p>to the <div id="container">. 


Part III In your Javascript file,
using setInterval,
call a function every 2 seconds. The function will add a new paragraph <p>Hello World</p>to the <div id="container">. 
The interval will be cleared (ie. clearInterval), when the user will click on the button. 
3.1 Instead of clicking on the button,
the interval will be cleared (ie. clearInterval) as soon as there will be 5 paragraphs inside the <div id="container">. */



//Part 1
// let timer = setTimeout(alertWord,2000)


// function alertWord(){
//     alert('Hello World')
// }

//Part 2
// let timer = setTimeout(newp, 2000)
// const containerMain = document.getElementById('container')

// function newp() {
//     containerMain.innerHTML = '<p>Hello World</p>'
// }

//Part 3
// let timer = setInterval(newp, 2000);
// const containerMain = document.getElementById('container');
// const button = document.getElementById('clear');
// button.addEventListener('click', function (){
//     clearInterval(timer)
// })

// function newp() {
//     const p = document.createElement('p')
//     p.innerText = 'Hello World'
//     containerMain.append(p)
// }

//Part 3.1
// let timer = setInterval(newp, 2000);
// const containerMain = document.getElementById('container');

// function newp() {
//     const p = document.createElement('p')
//     p.innerText = 'Hello World'
//     containerMain.append(p)
//     if (document.querySelectorAll('p').length >= 5) {
//         clearInterval(timer)
//     }
// }


const button = document.getElementsByTagName('button')[0];
const div = document.getElementById('container')
const element = document.getElementById('animate')

let move = 0;
let timer;

button.addEventListener('click', function () {
    timer = setInterval(moveBox, 10);
});

function moveBox() {
    move++;
    element.style.left = `${move}px`;

    const containerWidth = div.offsetWidth;
    const elementWidth = element.offsetWidth;

    if (move >= containerWidth - elementWidth) {
        clearInterval(timer);
    }
}