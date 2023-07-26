#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file

const fs = require('fs');
const request = require('request');
const rURL = process.argv[2];
const fileName = process.argv[3];

request.get(rURL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(fileName, body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
