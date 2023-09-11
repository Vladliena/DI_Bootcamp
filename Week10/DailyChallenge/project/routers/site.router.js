const express = require("express");
const router = express.Router();
const { getAllUsers, getUserById, createUser, updateUser, logUser } = require('../controllers/site.controller')

router.get("/", getAllUsers);

router.get('/:id', getUserById)

router.post("/register", createUser);

router.post("/login", logUser);

router.put("/:id", updateUser);


module.exports = { router }