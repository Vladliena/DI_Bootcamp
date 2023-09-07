const express = require("express");
const q_router = express.Router()
const { triviaQuestions } = require('../config/db')



let score = 0
let i = 0

q_router.get('/quiz', (req, res) => {
    if( i >= triviaQuestions.length){
        res.send(`Game is over, check your score at /quiz/score`)
    } else {
        res.json(triviaQuestions[i].question)
    }
});

q_router.post('/quiz', (req, res) => {
    if (i >= triviaQuestions.length) {
        res.send("Quiz is over. Check your score.");
    } else {
        const currentQuestion = triviaQuestions[i];
        const {answer} = req.body;
        if (answer.toLowerCase() === currentQuestion.answer.toLowerCase()) {
            score++;
            res.send("Correct answer!");
        } else {
            res.send("Incorrect answer!");
        }
        i++;
    }
});


q_router.get('/quiz/score', (req,res) => {
    res.send(`Your game is over! This is your score: ${score}`)
})
module.exports = {q_router}