const fs = require('fs');


fs.readdir('../file-explorer', (err, files) => {
    if (err)
        console.log(err);
    else {
        console.log("\nCurrent directory filenames:");
        files.forEach(file => {
            console.log(file);
        })
    }
})