#!/usr/bin/node
console.log(!isNaN(parseInt(process.argv[2])) ? `My number: ${parseInt(process.argv[2])}` : 'Not a number');
