const express = require('express');
const bcrypt = require('bcrypt');
const router = express.Router();
const { dataRead, dataWrite } = require('../fs-module/fileManager')



router.get('/', dataRead, (req, res) => {
    res.json(req.users)
})

router.get('/:id', dataRead, (req, res) => {
    const { id } = req.params;
    const user = req.users.find((user) => user.id == id);
    if (!user) return res.sendStatus(404).json({ msg: "User not found" });
    res.status(200).json(user);
})

router.put('/:id', dataRead, (req, res, next) => {
    const { id } = req.params;
    const { name, lastName, email, username, password } = req.body;
    if (!name || !lastName || !email || !username || !password) {
        return res.status(400).json({ msg: "All fields are required" });
    }
    const index = req.users.findIndex((user) => user.id == id);
    if (index === -1) return res.status(404).json({ msg: "not found" });
    req.users[index] = {
        ...req.users[index],
        name: name,
        lastName: lastName,
        email: email,
        username: username,
        password: password
    }
    next()
}, dataWrite, (res, req) => {
    res.json(req.users)
})


router.post('/register', dataRead, (req, res, next) => {
    const { name, lastName, email, username, password } = req.body;
    const existingUsers = req.users.find((user) => user.username === username)
    if (existingUsers) {
        return res.status(400).json({ message: 'Username already exists' });
    }
    const hashedPassword = bcrypt.hashSync(password, 10);
    const newUser = {
        id: req.tasks.length + 1,
        name: name,
        lastName: lastName,
        email: email,
        username: username,
        password: hashedPassword,
    };

    req.users.push(newUser);
    next()
}, dataWrite, (req, res) => {
    res.redirect('login.html');
})

router.post('/login', dataRead, (req, res) => {
    const { username, password } = req.body;
    const user = req.users.find((user) => user.username === username);
    if (!user) {
        return res.status(401).json({ message: 'No such user' });
    }
    if (bcrypt.compareSync(password, user.password)) {
        return res.redirect('hi.html')
    } else {
        return res.status(401).json({ message: 'Invalid password' });
    }
});




module.exports = router