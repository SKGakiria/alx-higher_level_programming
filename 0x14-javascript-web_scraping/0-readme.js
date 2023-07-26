#!/usr/bin/node
// script reads and prints the content of a file

const fs = require('fs');
const fileName = process.argv[2];

fs.readFile(fileName, 'utf-8', (error, f_content) => {
    if (error) {
      console.log(error);
    } else {
      console.log(f_content);
    }
});
