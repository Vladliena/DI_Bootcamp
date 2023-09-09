const express = require("express");
const t_router = express.Router()
const { dataRead, dataWrite } = require('../fs-module/fileManager')



t_router.get('/', dataRead, (req, res) => {
    res.json(req.tasks)
})

t_router.get('/:id', dataRead, (req, res) => {
    const { id } = req.params;
    const task = req.tasks.find((item) => item.id == id);
    if (!task) return res.sendStatus(404).json({ msg: "Product not found" });
    res.status(200).json(task);
})

t_router.post('/', dataRead, (req, res, next) => {
    const { id, title, task } = req.body;
    if (!title || !task) {
        return res.status(400).json({ msg: "All fields are required" });
    }
    req.tasks = req.tasks || []
    const newTask = {
        id: req.tasks.length + 1,
        title: title,
        task: task
    }
    req.tasks.push(newTask);
    next()
}, dataWrite, (req, res) => {
    res.json(req.tasks);
});

t_router.put('/:id', dataRead, (req, res, next) => {
    const { id } = req.params;
    const { title, task } = req.body
    if (!title || !task) {
        return res.status(400).json({ msg: "All fields are required" });
    }
    const index = req.tasks.findIndex((item) => item.id == id);
    if (index === -1) return res.status(404).json({ msg: "not found" });
    req.tasks[index] = {
        ...req.tasks[index],
        title: title,
        task: task
    }
    next()
}, dataWrite, (req, res) => {
    res.status(200).json(req.tasks);
})


t_router.delete('/:id', dataRead, (req, res, next) => {
    const { id } = req.params;
    const index = req.tasks.findIndex((item) => item.id == id);
    if (index === -1) return res.status(404).json({ msg: "not found" });
    req.tasks.splice(index, 1);
    next()
}, dataWrite, (req, res) => {
    res.status(200).json(req.tasks);
})



module.exports = { t_router }
