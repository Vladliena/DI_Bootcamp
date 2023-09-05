const fs = require('fs');



const txtData =  fs.readFileSync('./sourse.txt', 'utf-8', (err, data) => {
    if (err) {
        console.error(err);
    }
    return data
});

console.log(txtData)

fs.writeFile('destination.txt', txtData, (err) => {
    if (err) {
        console.error(err);
        return;
    }
});