const bcrypt = require('bcrypt');
const { db } = require("../config/db");

const _getAllUsers = () => {
    return db("users").select("id","username","email", "password")
};

const getUserByUsernamPassword = async (username) => {
    return db('users').where('username', username).first();
};

const _getUserById = (id) => {
    return db("users").select("id", "username", "email", "password").where({ id });
};


const _insertUser = ({ username, email, password }) => {
    const hashedPassword = bcrypt.hashSync(password, 10);
    return db("users").insert({ username, email, password: hashedPassword }, ["id", "username", "email", "password"]);
};

const _updateUser = ({ username, email, password }, id) => {
    const hashedPassword = bcrypt.hashSync(password, 10);
    return db("users")
        .update({ username, email, password: hashedPassword })
        .where({ id })
        .returning(["id", "username", "email", "password"]);
};

module.exports = {
    _getAllUsers,
    getUserByUsernamPassword,
    _getUserById,
    _insertUser,
    _updateUser,
};