const { _getAllPosts, _getPostById, _insertPost, _updatePost, _deletePost } = require('../models/posts.models')


const getAllPosts = (req, res) => {
    _getAllPosts()
        .then((data) => {
            res.json(data);
        })
        .catch((err) => {
            console.log(err);
            res.status(404).json({ msg: "not found" });
        });
};

const getPost = async (req, res) => {
    try {
        const {id} = req.params;
        const data = await _getPostById(id);
        res.json(data);
    } catch (error) {
        console.log(error);
        res.status(404).json({ msg: "no post match this id" });
    }
};

const createPost = async (req, res) => {
    try {
        const data = await _insertPost(req.body);
        res.json(data);
    } catch (error) {
        console.log(error);
        res.status(404).json({ msg: error.message });
    }
};

const updatePost = async (req, res) => {
    const { id } = req.params;
    const { title, content } = req.body;

    try {
        const data = await _updatePost(req.body, id);
        res.json(data);
    } catch (error) {
        console.log(error);
        res.status(404).json({ msg: error.message });
    }
};

const deletePost = async (req, res) => {
    const { id } = req.params;
    try {
        const data = await _deletePost(id);
        res.json(data);
    } catch (error) {
        console.log(error);
        res.status(404).json({ msg: error.message });
    }
};



module.exports = {getAllPosts,getPost, createPost, updatePost,deletePost}