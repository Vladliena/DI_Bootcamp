// 🌟 Exercise 1 : Change The Article
// Instructions
// Copy the code below, into a structured HTML file:

// <article>
//     <h1> Some Facts </h1>
//     <h2> The Chocolate </h2>
//     <h3> History of the chocolate </h3>
//     <p> Chocolate is made from tropical Theobroma cacao tree seeds.
//         Its earliest use dates back to the Olmec civilization in Mesoamerica.</p>
//     <p> After the European discovery of the Americas, chocolate became
//         very popular in the wider world, and its demand exploded. </p>
//     <p> Chocolate has since become a popular food product that millions enjoy every day,
//         thanks to its unique, rich, and sweet taste.</p>
//     <p> But what effect does eating chocolate have on our health?</p>
// </article>


// Using a DOM property, retrieve the h1 and console.log it.

// Using DOM methods, remove the last paragraph in the < article > tag.

// Add a event listener which will change the background color of the h2 to red, when it’s clicked on.

// Add an event listener which will hide the h3 when it’s clicked on(use the display: none property).

// Add a < button > to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.

//     BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)

// BONUS: When you hover on the 2nd paragraph, it should fade out(Check out “fade css animation” on Google)

const h1 = document.getElementsByTagName('h1')[0]
console.log(h1.textContent)
h1.addEventListener('mouseover', () => {
    h1.style.fontSize = `${Math.floor(Math.random() * (100 - 0)) + 0}px`;
})

const article = document.querySelector('article')
const lastP = article.querySelector('p:last-child')
article.removeChild(lastP)

const h2 = document.getElementsByTagName('h2')[0]
h2.addEventListener('click', function () {
    h2.style.backgroundColor = 'red'
})

const h3 = document.getElementsByTagName('h3')[0]
h3.addEventListener('click', function () {
    h3.style.display = 'none'
})

const button = document.createElement('button')
button.innerText = 'Click to make text bold'
article.appendChild(button)
button.addEventListener('click', () => {
    article.style.fontWeight = 'bold'
})

const p2 = document.getElementsByTagName('p')[1]
p2.addEventListener('mouseover', () => {
    p2.classList.toggle('fade');
})

// Second option for fadeOut effect

// p2.addEventListener('mouseover', fade)

// function fade(element) {
//     var opacity = 1;
//     var timer = setInterval(function () {
//         if (op <= 0.1) {
//             clearInterval(timer);
//             p2.style.display = 'none';
//         }
//         p2.style.opacity = opacity;
//         p2.style.filter = 'alpha(opacity=' + op * 100 + ")";
//         op -= op * 0.1;
//     }, 50);
// }


// 🌟 Exercise 2 : Work With Forms
// Instructions
// Copy the code below, into a structured HTML file:

// <form>
//     <label for="fname">First name:</label><br>
//         <input type="text" id="fname" name="firstname"><br>
//             <label for="lname">Last name:</label><br>
//                 <input type="text" id="lname" name="lastname"><br><br>
//                     <input type="submit" value="Submit" id="submit">
//                     </form>
//                     <ul class="usersAnswer"></ul>


//                     Retrieve the form and console.log it.

//                     Retrieve the inputs by their id and console.log them.

//                     Retrieve the inputs by their name attribute and console.log them.

//                     When the user submits the form (ie. submit event listener)
//                     use event.preventDefault(), why ?
//                     get the values of the input tags,
//                     make sure that they are not empty,
//                     create an li per input value,
//                     then append them to a the <ul class="usersAnswer"></ul>, below the form.
//                     The output should be :

//                     <ul class="usersAnswer">
//                         <li>first name of the user</li>
//                         <li>last name of the user</li>
//                     </ul>


const form = document.getElementsByTagName('form')[0];
console.log(form);

const fname = document.getElementById('fname');
console.log(fname);
const lname = document.getElementById('lname');
console.log(lname);

const fnameByName = form.elements.firstname;
console.log(fnameByName);
const lnameByName = form.elements.lastname;
console.log(lnameByName);

form.addEventListener('submit', function(e){
    e.preventDefault();
    const fnameValue = fname.value;
    const lnameValue = lname.value;
    const ul = document.querySelector('.usersAnswer')
    if (fnameValue && lnameValue){
        const fnameLi = document.createElement('li')
        fnameLi.innerText = fnameValue
        const lnameLi = document.createElement('li')
        lnameLi.innerText = lnameValue
        ul.append(fnameLi, lnameLi)
    }
})


// 🌟 Exercise 3 : Transform The Sentence
// Instructions
// Add this sentence to your HTML file then follow the steps:

// <p><strong>Hello</strong> I hope you are enjoying <strong>this</strong> class. At the
//     <strong>end</strong> you <strong>will</strong> be great Developers!
//     <strong>Enjoy</strong> the <strong>JavaScript </strong> lessons</p>


// In the JS file:

// Declare a global variable named allBoldItems.

// Create a function called getBoldItems() that takes no parameter.This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.

// Create a function called highlight() that changes the color of all the bold text to blue.

// Create a function called returnItemsToDefault() that changes the color of all the bold text back to black.

// Call the function highlight() on mouseover(ie.when the mouse pointer is moved onto the paragraph), and the function returnItemsToDefault() on mouseout(ie.when the mouse pointer is moved out of the paragraph).Look at this example



let allBoldItems = [];
const p = document.querySelector('p')


function getBoldItems() {
    allBoldItems = p.querySelectorAll('strong')
    console.log(allBoldItems)
}

function highlight() {
    allBoldItems.forEach((item) => {
        item.style.color = 'blue'
    })
}

function returnItemsToDefault(){
    allBoldItems.forEach((item) => {
        item.style.color = 'black'
    })
}

getBoldItems()
p.addEventListener('mouseover', highlight)
p.addEventListener('mouseout',returnItemsToDefault)

// 🌟 Exercice 4 : Volume Of A Sphere
// Instructions
// Write a JavaScript program to calculate the volume of a sphere.Use the code below as a base:
// < !doctype html >
//     <html lang="en">
//         <head>
//             <meta charset="utf-8">
//                 <title>Volume of a Sphere</title>
//                 <style>
//                     body {
//                         padding - top:30px;
//             }

//                     label,input {
//                         display:block;
//             }
//                 </style>
//         </head>
//         <body>
//             <p>Input radius value and get the volume of a sphere.</p>
//             <form id="MyForm">
//                 <label for="radius">Radius</label><input type="text" name="radius" id="radius" required>
//                     <label for="volume">Volume</label><input type="text" name="volume" id="volume">
//                         <input type="submit" value="Calculate" id="submit">
//                         </form>
//                     </body>
//                 </html> 


const myForm = document.getElementById('MyForm')
const radius = myForm.elements.radius
const volume = myForm.elements.volume
myForm.addEventListener('submit', function (e) {
    e.preventDefault()
    const pi = Math.PI;
    const volumeMain = (4 / 3) * pi * Math.pow(radius.value, 3);
    volume.value = volumeMain.toFixed(2);
    return
})

// Exercise 5 : Event Listeners
// Instructions
// Add many events listeners to one element on your webpage.Use the click, mouseover, mouseout and dblclick events.
// Each listener should do a different thing, for instance - change position x, change position y, change color, change the font size… and more.

const button = document.getElementById('Button')

button.addEventListener("mouseover", () => {
    button.style.fontSize = `10px`;
    button.style.color = 'red'
});

button.addEventListener("click", () => {
    button.style.backgroundColor = 'blue';
    button.style.position = 'absolute';
    button.style.top = '100px';
    button.style.left = '300px';
});


button.addEventListener("mouseout", () => {
    button.style.fontSize = "16px";
    button.style.backgroundColor = "pink";
});

