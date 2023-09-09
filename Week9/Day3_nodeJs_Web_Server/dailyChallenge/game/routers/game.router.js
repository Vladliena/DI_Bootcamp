const express = require('express')
const router = express.Router()
const {emojis} = require('../config/db')

function generateRandomEmoji() {
    const randomIndex = Math.floor(Math.random() * emojis.length);
    let currentEmoji = emojis[randomIndex];
    return currentEmoji
}


module.exports = {router}