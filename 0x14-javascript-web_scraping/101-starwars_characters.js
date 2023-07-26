#!/usr/bin/node
// script prints all characters of a Star Wars movie

const request = require('request');
const movieID = process.argv[2];
const apiURL = `https://swapi.dev/api/films/${movieID}/`;
let characters = [];

request(apiURL, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const mData = JSON.parse(body);
  characters = mData.characters;
  getCharacters(0);
});

const getCharacters = (index) => {
  if (index === characters.length) {
    return;
  }

  request(characters[index], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const characterData = JSON.parse(body);
    console.log(characterData.name);
    getCharacters(index + 1);
  });
};
