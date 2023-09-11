const bcrypt = require('bcrypt');
const { _getAllUsers,
    getUserByUsernamPassword,
    _getUserById,
    _insertUser,
    _updateUser, } = require('../models/site.models')



const getAllUsers = (req, res) => {
    _getAllUsers()
        .then((data) => {
            res.json(data);
        })
        .catch((err) => {
            console.log(err);
            res.status(404).json({ msg: "not found" });
        });
};

const logUser = async (req, res) => {
    const { username, password } = req.body;

    try {
        const user = await getUserByUsernamPassword(username);

        if (!user) {
            return res.status(401).json({ message: 'No such user' });
        }
        if (bcrypt.compareSync(password, user.password)) {
            return res.json({ message: 'Login successful' });
        } else {
            return res.status(401).json({ message: 'Invalid password' });
        }
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Internal server error' });
    }
}

const getUserById = async (req, res) => {
    try {
        const { id } = req.params;
        const data = await _getUserById(id);
        res.json(data);
    } catch (error) {
        console.log(error);
        res.status(404).json({ msg: "no post match this id" });
    }
};

const createUser = async (req, res) => {
    try {
        const data = await _insertUser(req.body);
        res.json(data);
    } catch (error) {
        console.log(error);
        res.status(404).json({ msg: error.message });
    }
};

const updateUser = async (req, res) => {
    const { id } = req.params;
    const { username, email, password } = req.body;

    try {
        const data = await _updateUser(req.body, id);
        res.json(data);
    } catch (error) {
        console.log(error);
        res.status(404).json({ msg: error.message });
    }
};




module.exports = { getAllUsers, getUserById, createUser, updateUser, logUser }