#!/usr/bin/node
const request = require('request');
const targetURL = process.argv[2];

request.get(targetURL, (err, res, body) => {
  if (err) console.log(err);
  console.log(`code: ${res.statusCode}`);
});
