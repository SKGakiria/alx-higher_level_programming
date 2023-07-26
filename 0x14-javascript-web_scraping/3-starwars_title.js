#!/usr/bin/node
// script prints the title of a Star Wars movie
// where the episode number matches a given integer

const request = require('request');
const movieID = process.argv[2];
const rURL = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(rURL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const mData = JSON.parse(body);
    console.log(mData.title);
  }
});
