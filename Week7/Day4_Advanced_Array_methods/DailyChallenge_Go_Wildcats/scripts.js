// Instructions
// Using this array:

const gameInfo = [
    {
        username: "john",
        team: "red",
        score: 5,
        items: ["ball", "book", "pen"]
    },
    {
        username: "becky",
        team: "blue",
        score: 10,
        items: ["tape", "backpack", "pen"]
    },
    {
        username: "susy",
        team: "red",
        score: 55,
        items: ["ball", "eraser", "pen"]
    },
    {
        username: "tyson",
        team: "green",
        score: 1,
        items: ["book", "pen"]
    },
];
// 1. Create an array using forEach that contains all the usernames from the gameInfo array, add an exclamation point(ie. “!”) to the end of every username.
// The new array should look like this :
// const usernames = ["john!", "becky!", "susy!", "tyson!"]


// 2. Create an array using forEach that contains the usernames of all players with a score bigger than 5.
// The new array should look like this :

// const winners = ["becky", "susy"]


// 3. Find and display the total score of the users. (Hint: The total score is 71)

//1:
const newArray1 = []
gameInfo.forEach((names) => {
    newArray1.push(`${names.username}!`)
})

console.log(newArray1)

//2:
const newArray2 = [];
gameInfo.forEach(element => {
    (element.score > 5) && newArray2.push(element.username);
})

console.log(newArray2)

//3:
let score = 0
gameInfo.forEach(element => {
    score += element.score
})

console.log(score)