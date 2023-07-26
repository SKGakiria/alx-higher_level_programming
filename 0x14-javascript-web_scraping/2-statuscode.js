#!/usr/bin/node
// script displays the status code of a GET request

const request = require('request');
const r_url = process.argv[2];

request.get(r_url, (error, response) => {
    if (error) {
      console.log(error);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
});
