const express = require('express')
const { books } = require('./db')
const app = express()
const dotenv = require('dotenv')
dotenv.config();
app.use(express.urlencoded({ extended: true }))
app.use(express.json())



app.listen(process.env.PORT, () => {
    console.log(`run on port ${process.env.PORT}`)
});

app.get('/api/books', (req, res) => {
    res.json(books);
});

app.get('/api/books/:id', (req, res) => {
    const { id } = req.params
    const book = books.find((item) => item.id == id)
    if (!book) {
        return res.status(404).json({ msg: 'no such post' })
    } else {
        res.json(book)
        res.status(200).json({ msg: "OK" })
    }
});


app.post('/api/books', (req, res) => {
    const { title, author, publishedYear } = req.body;
    const book = {
        id: books.length + 1,
        title: title,
        author: author,
        publishedYear: publishedYear
    }
    books.push(book)
    res.json(books)
})
