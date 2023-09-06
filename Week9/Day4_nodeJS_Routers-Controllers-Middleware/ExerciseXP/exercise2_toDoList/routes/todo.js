const express = require('express')
const router = express.Router()
const { todos } = require('../config/db')

router.get('/', (req, res) => {
    res.json(todos)
});

router.post('/', (req, res) => {
    const { task, deadline } = req.body;
    const newToDo = {
        id: todos.length + 1,
        task: task,
        deadline: deadline
    }
    todos.push(newToDo)
    res.json(todos)
})

router.put('/:id', (req, res) => {
    const { id } = req.params;
    const { task, deadline } = req.body;
    const index = todos.findIndex((item) => item.id == id);
    todos[index] = {
        ...todos[index],
        task: task,
        deadline: deadline,
    };
    res.json(todos);
});

router.delete('/:id', (req, res) => {
    const { id } = req.params;
    const index = todos.findIndex((item) => item.id == id);
    if (index === -1) {
        return res.status(404).json({ error: 'Todo not found' });
    }
    todos.splice(index, 1);
    res.json(todos);
});


module.exports = { router }