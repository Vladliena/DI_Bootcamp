import myArrLocation from "./data.js";

function getAverage(data) {
    const average = data.reduce((total, el) => total + el.age, 0) / data.length;
    return average
}

console.log(getAverage(myArrLocation))


// for exercise 2 "type": "module" in package.json