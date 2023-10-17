#!/usr/bin/node
/**
 * This class represents a square and inherits from Square
 * of 5-rectangle.js
 */

const PreviousSquare = require('./5-square.js');
class Square extends PreviousSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let a = 0; a < this.height; a++) {
      let myVar = '';
      for (let b = 0; b < this.width; b++) {
        myVar += c;
      }
      console.log(myVar);
    }
  }
}
module.exports = Square;
