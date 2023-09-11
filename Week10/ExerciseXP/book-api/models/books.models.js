const { db } = require("../config/db");

const _getAllBooks = () => {
    return db("books").select("id", "title", "author", "publishedyear").orderBy("title");
};

const _getBookById = (id) => {
    return db("books").select("id", "title", "author", "publishedyear").where({ id });
};


const _insertBook = ({ title, author, publishedyear }) => {
    return db("books").insert({ title, author, publishedyear }, ["id", "title", "author", "publishedyear"]);
};

const _updateBook = ({ title, author, publishedyear }, id) => {
    return db("books")
        .update({ title, author, publishedyear })
        .where({ id })
        .returning(["id", "title", "author", "publishedyear"]);
};

const _deleteBook = (id) => {
    return db("books").where({ id }).del().returning(["id", "title", "author", "publishedyear"]);
};

module.exports = {
    _getAllBooks,
    _getBookById,
    _insertBook,
    _updateBook,
    _deleteBook
};