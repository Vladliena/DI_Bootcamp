const express = require('express')
const app = express()
const {router} = require('./routes/todo')
app.use(express.json())

app.listen(5000, () => {
    console.log(`run on port 5000`);
});

app.use('/todos', router)
