#!/usr/bin/node
export.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let x = 0; x < list.length; x++) {
    counter = (list[x] === searchElement ? counter + 1 : counter);
  }
  return counter;
};
