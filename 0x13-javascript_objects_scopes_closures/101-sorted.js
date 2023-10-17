#!/usr/bin/node
const dict = require('./101-data.js').dict;

const nDict = {};

Object.getOwnPropertyNames(dict).forEach(occurences => {
  if (nDict[dict[occurences]] === undefined) {
    nDict[dict[occurences]] = [occurences];
  } else {
    nDict[dict[occurences]].push(occurences);
  }
});
console.log(nDict);
