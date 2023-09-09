const express = require('express');
const bcrypt = require('bcrypt');
const fs = require('fs');
app = express()
app.use(express.urlencoded({ extended: true }));
app.use(express.json())
const router = require('./routes/server.router')
const path = require('path');
PORT = 3000


function errorHandler(err, req, res, next) {
    console.error(err.stack);
    res.status(500).send('Something went wrong!');
}

app.use(errorHandler);

app.listen(PORT, () => {
    console.log(`Listen on ${PORT}`)
})


app.use('/', router)
app.use(express.static('public'));