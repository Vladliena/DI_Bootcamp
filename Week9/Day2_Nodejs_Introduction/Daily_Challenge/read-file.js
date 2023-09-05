import fs from 'fs'

function readFileContent() {
    fs.readFile('./file-data.txt', 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading the file:', err);
            return;
        }
        console.log('File text -', data);
    });
}

// module.exports = readFileContent;
export default readFileContent