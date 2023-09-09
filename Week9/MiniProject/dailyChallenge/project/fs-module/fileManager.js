const fs = require('fs');


function dataRead(req, res, next) {
    fs.readFile('./fs-module/users.json', 'utf8', (err, data) => {
        if (err) {
            next(err);
        } else {
            req.users = JSON.parse(data) || [];
            next();
        }
    });
}

function dataWrite(req, res, next) {
    const users = req.users;
    fs.writeFile('./fs-module/users.json', JSON.stringify(users), 'utf8', (err) => {
        if (err) {
            next(err);
        } else {
            next();
        }
    });
}

module.exports = { dataRead, dataWrite };