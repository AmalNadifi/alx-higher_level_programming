#!/usr/bin/node
const fs = require('fs');

// Read the file specified in the command line argument
fs.readFile(process.argv[2], 'utf8', function (err, data) {
	// Log either the error or the content to the console
	// console.log(err || data);
});
