const express = require('express')
const router = express.Router()
const { emojis } = require('../config/db')


let totlScore = 0
let currentEmoji = null;

function randomEmoji() {
    let randomIndex = Math.floor(Math.random() * emojis.length);
    currentEmoji = emojis[randomIndex];
}

function distractors() {
    const distractors = []
    const currentEmojiName = currentEmoji.name

    for (let i = 0; i < 4; i++) {
        let randomIndex; // Declare randomIndex outside the do...while block

        do {
            randomIndex = Math.floor(Math.random() * emojis.length);
        } while (emojis[randomIndex].name === currentEmojiName || distractors.includes(emojis[randomIndex].name))

        distractors.push(emojis[randomIndex].name)
    }

    return distractors
}


router.get('/game', (req, res) => {
    randomEmoji();
    let options = distractors()
    console.log(options)
    // const options = [...distractors()];
    // res.json({ emoji: currentEmoji.emoji, options });
});

router.post('/guess', (req, res) => {
    const guess = req.body.guess;
    if (guess === currentEmoji.name) {
        totalScore++;
        res.json({ message: 'Correct!', score });
    } else {
        res.json({ message: 'Incorrect! The correct answer is ' + currentEmoji.name, score });
    }
});

router.get('/score', (req, res) => {
    res.json({ score });
});


module.exports = { router }