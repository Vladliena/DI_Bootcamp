const express = require('express')
const app = express()
const cors = require("cors");
const dotenv = require('dotenv')
const {b_router} = require('./routes/book.router')
dotenv.config()
app.use(express.urlencoded({ extended: true }));
app.use(express.json())
app.use(cors());


app.listen(process.env.PORT, () => {
    console.log(`Listen on port ${process.env.PORT}`)
})


app.use('/books', b_router)