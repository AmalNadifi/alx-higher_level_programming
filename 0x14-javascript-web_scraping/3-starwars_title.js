#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + filmId;

request(apiUrl, (err, res, body) => {
  if (err) console.log(err);

  const filmData = JSON.parse(body);
  console.log(filmData.title);
});
