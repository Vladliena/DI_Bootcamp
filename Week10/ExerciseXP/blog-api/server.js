const express = require('express')
const app = express()
const cors = require("cors");
const dotenv = require('dotenv')
dotenv.config()
const {p_router} = require('./routes/posts.router')
app.use(express.urlencoded({ extended: true }));
app.use(express.json())
app.use(cors());


app.listen(process.env.PORT, () => {
    console.log(`Listen on port ${process.env.PORT}`)
})


app.use('/posts', p_router)

