#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (err, res, body) => {
  if (!err) {
    const films = JSON.parse(body).results;
    const filmsWithCharacter18 = films.filter(film => {
      for (const characterUrl of film.characters) {
        if (characterUrl.endsWith('/18/')) {
          return true;
        }
      }
      return false;
    });
    console.log(filmsWithCharacter18.length);
  }
});
