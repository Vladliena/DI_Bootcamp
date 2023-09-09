const express = require('express');
const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
const dotenv = require("dotenv");
dotenv.config();
const { t_router } = require('./routes/tasks.router')


function errorHandler(err, req, res, next) {
    console.error(err.stack);
    res.status(500).send('Something went wrong!');
}

app.use(errorHandler);

app.listen(process.env.PORT, () => {
    console.log(`listen on port ${process.env.PORT}`)
})


app.use('/tasks', t_router)

