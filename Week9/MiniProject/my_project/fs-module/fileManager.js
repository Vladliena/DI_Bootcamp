const fs = require('fs');

function dataRead(req, res, next) {
    fs.readFile('./fs-module/task.json', 'utf8', (err, data) => {
        if (err) {
            next(err);
        } else {
            req.tasks = JSON.parse(data) || [];
            next();
        }
    });
}

function dataWrite(req, res, next) {
    const tasks = req.tasks;
    fs.writeFile('./fs-module/task.json', JSON.stringify(tasks), 'utf8', (err) => {
        if (err) {
            next(err);
        } else {
            next();
        }
    });
}

module.exports = { dataRead, dataWrite };