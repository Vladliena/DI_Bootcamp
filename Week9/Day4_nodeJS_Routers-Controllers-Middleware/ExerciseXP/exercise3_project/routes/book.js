const express = require('express')
const routerBook = express.Router()

routerBook.get('/', (req, res) => {
    res.json(books);
});

routerBook.post('/', (req, res) => {
    const { title, author } = req.body;
    if (!title || !author) {
        return res.status(400).json({ error: 'title and author are required' });
    }
    const newBook = { id: books.length + 1, title:title, author:author };
    books.push(newBook);
    res.json(books)
});

routerBook.put('/:id', (req, res) => {
    const { id } = req.params;
    const { title, author } = req.body;
    const index = books.findIndex((item) => item.id == id);
    books[index] = {
        ...books[index],
        title: title, 
        author: author
    };
    res.json(books);
});

routerBook.delete('/:id', (req, res) => {
    const { id } = req.params;
    const index = books.findIndex((item) => item.id == id);
    if (index === -1) {
        return res.status(404).json({ error: 'Todo not found' });
    }
    books.splice(index, 1);
    res.json(books);
});

const books = [];

module.exports = {routerBook}