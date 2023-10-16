#!/usr/bin/node
const counter = process.argv.length;

if (counter > 2) {
  console.log('Argument' + (counter > 3 ? 's' : '') + ' found');
} else {
  console.log('No argument');
}
