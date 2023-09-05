const fs = require('fs');


const dataRead = () => {
    fs.readFile('HelloWorld.txt', 'utf-8', (err, data) => {
        if (err) return console.log(err);
        console.log(data)
    });
}


const data = 'Bye World'

const dataWrite = () => { fs.writeFile("data.json", JSON.stringify(data), (err) => err && console.error(err)); }


module.exports = { dataRead, dataWrite }

