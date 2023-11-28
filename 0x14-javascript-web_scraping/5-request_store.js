#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const outputPath = process.argv[3];

// Make a GET request to the specified URL and pipe the response to a file
request(url).pipe(fs.createWriteStream(outputPath));
