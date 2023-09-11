const express = require("express");
const b_router = express.Router();
const { getAllBooks, getBookById, createBook, updateBook, deleteBook } = require('../controllers/books.controller')

b_router.get("/", getAllBooks);

b_router.get('/:id', getBookById)

b_router.post("/", createBook);

b_router.put("/:id", updateBook);

b_router.delete("/:id", deleteBook);

module.exports = { b_router }