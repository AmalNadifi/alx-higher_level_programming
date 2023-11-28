#!/usr/bin/node

const request = require('request');
const util = require('util');

const filmId = process.argv[2];
const filmApiUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

const prequest = util.promisify(request);

(async () => {
  try {
    const filmData = (await prequest(filmApiUrl, { json: true })).body;

    // Function to retrieve and log character names
    const logCharacterName = async (charURL) => {
      try {
        const characterData = (await prequest(charURL, { json: true })).body;
        console.log(characterData.name);
      } catch (errorChar) {
        console.error(errorChar);
      }
    };

    // Log names of characters asynchronously
    await Promise.all(filmData.characters.map(logCharacterName));
  } catch (errorFilm) {
    console.error(errorFilm);
  }
})();
