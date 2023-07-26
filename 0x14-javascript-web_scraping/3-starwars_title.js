#!/usr/bin/node
// script prints the title of a Star Wars movie
// where the episode number matches a given integer

const request = require('request');
const movie_id = process.argv[2];
const r_url = `https://swapi-api.alx-tools.com/api/films/${movie_id}`;

request.get(r_url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const mData = JSON.parse(body);
    console.log(mData.title);
  }
});
