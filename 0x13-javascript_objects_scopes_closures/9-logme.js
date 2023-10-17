#!/usr/bin/node

let ctr = 0;

exports.logMe = function count (item) {
  console.log(`${ctr}: ${item}`);
  ctr += 1;
};
