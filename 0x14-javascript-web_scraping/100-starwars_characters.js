#!/usr/bin/node
// script prints all characters of a Star Wars movie

const request = require('request');
const movieID = process.argv[2];
const apiURL = `https://swapi.dev/api/films/${movieID}/`;

request.get(apiURL, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const mData = JSON.parse(body);
  const characters = mData.characters;
  for (const character of characters) {
    request.get(character, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  }
});
