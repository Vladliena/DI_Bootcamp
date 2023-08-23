// 🌟 Exercise 1 : Scope
// Instructions
// Analyse the code below, and predict what will be the value of a in all the following functions.
// Write your prediction as comments in a js file.Explain your predictions.
// // #1
// function funcOne() {
//     let a = 5;
//     if (a > 1) {
//         a = 3;
//     }
//     alert(`inside the funcOne function ${a}`);
// }

//#1 Answer - If we run this function in alert we will have a = 3


// // #1.1 - run in the console:
// funcOne()
// // #1.2 What will happen if the variable is declared
// // with const instead of let ?

//#1.1 Answer - we will have an error because we are trying to overwrite a CONST variable

// //#2
// let a = 0;
// function funcTwo() {
//     a = 5;
// }

// function funcThree() {
//     alert(`inside the funcThree function ${a}`);
// }

// #2 Answer - funcTwo will overwrite global variable 'a' and funcThree will give us alert with a=5

// // #2.1 - run in the console:
// funcThree()
// funcTwo()
// funcThree()

// #2.1 Answer - alert with 0 and second alert with 5


// // #2.2 What will happen if the variable is declared
// // with const instead of let ?


// #2.2 Answer - 1 alert will be with 0 and then we will have assignment error


// //#3
// function funcFour() {
//     window.a = "hello";
// }


// function funcFive() {
//     alert(`inside the funcFive function ${a}`);
// }

// #3 Answer - We are trying to overwrite type of global variable 'a'

// // #3.1 - run in the console:
// funcFour()
// funcFive()

// #3.1 Answer - alert will be a = 0, because funcFour can't overwrite type number to string


// //#4
// let a = 1;
// function funcSix() {
//     let a = "test";
//     alert(`inside the funcSix function ${a}`);
// }

// #4 Answer -  for alert we are using 'a' (a='test') which is inside the function. Let a global and let a in function, are two different variables


// // #4.1 - run in the console:
// funcSix()

// #4.1 Answer - We will see alert: inside the funcSix function test

// // #4.2 What will happen if the variable is declared
// // with const instead of let ?

// #4.2 Answer - Nothing will change and stay as it was. We will still have alert: inside the funcSix function test. Since it will use a inside the function

// //#5
// const a = 2;
// if (true) {
//     let a = 5;
//     alert(`in the if block ${a}`);
// }
// alert(`outside of the if block ${a}`);

// #5 Answer - 1 alert: in the if block will be 5. 2 Alert: outside of the if block will be 2


// // #5.1 - run the code in the console
// // #5.2 What will happen if the variable is declared
// // with const instead of let ?


// #5.1 Answer - It will give an error like I'm trying to declaire a again (a has already been declaired). It is probably because js engine in console.log and in vscode works in a little different way. In browser it is probably more strict.

// #5.2 Answer - Same answer as #5 answer. Since it is a different variables


// 🌟 Exercise 2 : Ternary Operator
// Instructions
// Using the code below:

// function winBattle() {
//     return true;
// }
// Transform the winBattle() function to an arrow function.
// Create a variable called experiencePoints.
// Assign to this variable, a ternary operator.If winBattle() is true, the experiencePoints variable should be equal to 10, else the variable should be equal to 1.
// Console.log the experiencePoints variable.

const winBattle = () => true
let experiencePoints = winBattle() ? 10 : 1
console.log(experiencePoints)

// 🌟 Exercise 3 : Is It A String ?
//     Instructions
// Write a JavaScript arrow function that checks whether the value of the argument passed, is a string or not.The function should return true or false
// Check out the example below to see the expected output
// Example:

// console.log(isString('hello'));
// //true
// console.log(isString([1, 2, 4, 0]));
// //false

const isString = (param) => typeof param === 'string' ? true : false
console.log(isString([1, 2, 4, 0]))

// 🌟 Exercise 4 : Find The Sum
// Instructions
// Create a one line function (ie.an arrow function) that receives two numbers as parameters and returns the sum.

const sum = (a, b) => a + b
console.log(sum(2, 2))

// 🌟 Exercise 5 : Kg And Grams
// Instructions
// Create a function that receives a weight in kilograms and returns it in grams. (Hint: 1 kg is 1000gr)

// First, use function declaration and invoke it.
//     Then, use function expression and invoke it.
// Write in a one line comment, the difference between function declaration and function expression.
// Finally, use a one line arrow function and invoke it.

function getGrams(kg) {
    return kg * 1000
}

console.log(getGrams(2))

const getGrams = function (kg) {
    return kg * 1000
}

//Comments - function declarations are hoisted. Function expressions aren't hoisted.

console.log(getGrams(2))

const getGrams = (kg) => kg * 1000
console.log(getGrams(2))

    // 🌟 Exercise 6 : Fortune Teller
    // Instructions
    // Create a self invoking function that takes 4 arguments: number of children, partner’s name, geographic location, job title.
    // The function should display in the DOM a sentence like "You will be a <job title> in <geographic location>, and married to <partner's name> with <number of children> kids."


    (function (childrenNumber, partnerName, geoLocation, jobTitle) {
        let body = document.querySelector('body')
        let p = document.createElement('p')
        p.innerText = `You will be a ${jobTitle} in ${geoLocation}, and married to ${partnerName} with ${childrenNumber} kids.`
        body.appendChild(p)
    })(6, 'Valeriya', 'US', 'realtor')

// 🌟 Exercise 7 : Welcome
// Instructions
// John has just signed in to your website and you want to welcome him.

// Create a Navbar in your HTML file.
// In your js file, create a self invoking funtion that takes 1 argument: the name of the user that just signed in.
// The function should add a div in the nabvar, displaying the name of the user and his profile picture.

let form = document.getElementById('main_form');
let navbar = document.getElementById('navbar');

form.addEventListener('submit', function (event) {
    event.preventDefault();

    const userName = form.elements.name.value;

    (function (name) {
        let div = document.createElement('div');
        div.innerHTML = `<p>Hi ${name}</p>`;
        navbar.appendChild(div);
    })(userName);
});

// 🌟 Exercise 8 : Juice Bar
// Instructions
// You will use nested functions, to open a new juice bar.

// Part I:
// The outer function named makeJuice receives 1 argument: the size of the beverage the client wants - small, medium or large.

// The inner function named addIngredients receives 3 ingredients, and displays on the DOM a sentence like The client wants a < size drink > juice, containing < first ingredient >, <second ingredient>, <third ingredient>".

//     Invoke the inner function ONCE inside the outer function. Then invoke the outer function in the global scope.


//     Part II:
//     In the makeJuice function, create an empty array named ingredients.

//     The addIngredients function should now receive 3 ingredients, and push them into the ingredients array.

//     Create a new inner function named displayJuice that displays on the DOM a sentence like The client wants a <size drink> juice, containing <first ingredient>, <second ingredient>, <third ingredient>".

//         The client wants 6 ingredients in his juice, therefore, invoke the addIngredients function TWICE. Then invoke once the displayJuice function. Finally, invoke the makeJuice function in the global scope.


// Part 1

let body = document.querySelector('body')

function makeJuice(beverageSize) {
    function addIngredients(firstIngredient, secondIngredient, thirdIngredient) {
        let p = document.createElement('p')
        p.innerText = `The client wants a ${beverageSize} juice, containing ${firstIngredient}, ${secondIngredient}, ${thirdIngredient}`
        body.appendChild(p)
    }
    addIngredients('apple', 'peach', 'pineapple')
}

makeJuice('small')




// Part 2


let body = document.querySelector('body')

function makeJuice(beverageSize) {
    let ingredients = [];

    function addIngredients(firstIngredient, secondIngredient, thirdIngredient) {
        ingredients.push(firstIngredient, secondIngredient, thirdIngredient);
    }

    function displayJuice() {
        let p = document.createElement('p');
        p.innerText = `The client wants a ${beverageSize} juice, containing ${ingredients.join(', ')}`;
        document.body.appendChild(p);
    }

    addIngredients('apple', 'orange', 'carrot');
    addIngredients('strawberry', 'banana', 'spinach');
    displayJuice();
}

makeJuice('large');