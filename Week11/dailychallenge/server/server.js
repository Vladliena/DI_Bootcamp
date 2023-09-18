const express = require('express')
const app = express()

const cors = require('cors');
app.use(express.urlencoded({ extended: true }))
app.use(express.json())
app.use(cors());


app.listen(3000, () => {
    console.log(`run on port ${3000}`)
});

app.get('/api/hello', (req, res) => {
    res.json('Hello from Express')
});

app.post('/api/world', (req, res) => {
    const { input } = req.body;
    const responseMessage = `Your response message is ${input}`
    console.log('Request', req.body)
    res.json({ mesageServer: responseMessage })
})