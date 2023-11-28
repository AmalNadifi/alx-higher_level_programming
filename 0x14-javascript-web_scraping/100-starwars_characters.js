#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const filmApiUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request(filmApiUrl, (errorFilm, responseFilm, bodyFilm) => {
  if (!errorFilm) {
    const filmData = JSON.parse(bodyFilm);
    const characters = filmData.characters;

    // Function to retrieve and log character names
    const logCharacterName = (charURL) => {
      request(charURL, (errorChar, responseChar, bodyChar) => {
        if (!errorChar) {
          const characterData = JSON.parse(bodyChar);
          console.log(characterData.name);
        }
      });
    };

    // Log names of characters asynchronously
    characters.forEach(logCharacterName);
  }
});
