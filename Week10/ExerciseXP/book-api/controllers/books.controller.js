const { _getAllBooks,
    _getBookById,
    _insertBook,
    _updateBook,
    _deleteBook } = require('../models/books.models')


const getAllBooks = (req, res) => {
    _getAllBooks()
        .then((data) => {
            res.json(data);
        })
        .catch((err) => {
            console.log(err);
            res.status(404).json({ msg: "not found" });
        });
};

const getBookById = async (req, res) => {
    try {
        const { id } = req.params;
        const data = await _getBookById(id);
        res.json(data);
    } catch (error) {
        console.log(error);
        res.status(404).json({ msg: "no post match this id" });
    }
};

const createBook = async (req, res) => {
    try {
        const data = await _insertBook(req.body);
        res.json(data);
    } catch (error) {
        console.log(error);
        res.status(404).json({ msg: error.message });
    }
};

const updateBook = async (req, res) => {
    const { id } = req.params;
    const { title, author, publishedYear } = req.body;

    try {
        const data = await _updateBook(req.body, id);
        res.json(data);
    } catch (error) {
        console.log(error);
        res.status(404).json({ msg: error.message });
    }
};

const deleteBook = async (req, res) => {
    const { id } = req.params;
    try {
        const data = await _deleteBook(id);
        res.json(data);
    } catch (error) {
        console.log(error);
        res.status(404).json({ msg: error.message });
    }
};



module.exports = { getAllBooks, getBookById, createBook, updateBook, deleteBook }