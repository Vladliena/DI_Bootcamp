const express = require('express')
app = express()
app.use(express.urlencoded({ extended: true }));
app.use(express.json())
const {router} = require('./routers/game.router')
PORT = 3000

app.use(express.static('public'));
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});


app.listen(PORT, () => {
    console.log(`Listen on ${PORT}`)
})


app.use('/',router)
