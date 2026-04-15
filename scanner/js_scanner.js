const fs = require('fs');

function scan(file) {
    const data = fs.readFileSync(file, 'utf8');

    if (data.includes("eval(")) {
        console.log(`[!] JS Vulnerability in ${file} -> eval usage`);
    }
}

scan("../samples/test.js");