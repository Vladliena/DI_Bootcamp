const express = require('express')
const router = express.Router()
const { emojis } = require('../config/db')


let totalScore = 0
let currentEmoji = null;

function randomEmoji() {
    let randomIndex = Math.floor(Math.random() * emojis.length);
    currentEmoji = emojis[randomIndex];
}

function distractors() {
    const distractors = []
    const currentEmojiName = currentEmoji.name

    while ((distractors.length < 4)) {
        let randomIndex = Math.floor(Math.random() * emojis.length)
        console.log(randomIndex, emojis[randomIndex].name, currentEmojiName)
        if (emojis[randomIndex].name != currentEmojiName && !distractors.includes(emojis[randomIndex].name)) {
            console.log(distractors)
            distractors.push(emojis[randomIndex].name)
        }
    }
    console.log('done')
    return distractors
}


router.get('/game', (req, res) => {
    randomEmoji();
    let options = [currentEmoji.name, ...distractors()]
    res.json({ emoji: currentEmoji.emoji, options });
});

router.post('/guess', (req, res) => {
    const {name} = req.body;
    if (name == currentEmoji.name) {
        totalScore++;
        res.json({ message: 'Correct!', totalScore });
    } else {
        res.json({ message: 'Incorrect! The correct answer is ' + currentEmoji.name, totalScore });
    }
});

router.get('/score', (req, res) => {
    res.json({ totalScore });
});


module.exports = { router }