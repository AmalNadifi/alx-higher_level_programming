#!/usr/bin/node
/**
 * This class represents a rectangle with width and height attributes
 * Checking the parameters provided
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let a = 0; a < this.height; a++) {
      let myVar = '';
      let b = 0;
      while (b < this.width) {
        myVar += 'X';
        b++;
      }
      console.log(myVar);
    }
  }

  rotate () {
    let a = 0;
    a = this.width;
    this.width = this.height;
    this.height = a;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
