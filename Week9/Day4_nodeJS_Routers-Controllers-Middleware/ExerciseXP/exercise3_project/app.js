const express = require('express');
const { routerBook } = require('./routes/book')
const app = express();
const port = 3000;
app.use(express.json())


app.listen(port, () => {
    console.log(`server is runnin on ${port}`)
})


app.use('/books', routerBook)