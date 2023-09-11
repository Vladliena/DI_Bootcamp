const express = require("express");
const p_router = express.Router();
const { getAllPosts, getPost, createPost, updatePost, deletePost } = require('../controllers/posts.controllers')

p_router.get("/", getAllPosts);

p_router.get('/:id', getPost)

p_router.post("/", createPost);

p_router.put("/:id", updatePost);

p_router.delete("/:id", deletePost);

module.exports = {p_router}