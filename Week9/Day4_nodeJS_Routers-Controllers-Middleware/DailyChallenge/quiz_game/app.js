const express = require('express')
const app = express()
const dotenv = require("dotenv");
const {q_router} = require('./routes/quiz.router')
dotenv.config();
app.use(express.urlencoded({ extended: true }));
app.use(express.json())


app.listen(process.env.PORT, () => {
    console.log(`Listen on ${process.env.PORT}`)
})

app.use('/questions', q_router)

