#!/usr/bin/node
// script prints the number of movies
// where the character “Wedge Antilles” is present

const request = require('request');
const apiURL = process.argv[2];
const characterID = '18';
let count = 0;

request.get(apiURL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const filmData = JSON.parse(body);
    filmData.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(characterID)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
