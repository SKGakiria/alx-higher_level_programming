#!/usr/bin/node
// defines a class Square that inherits from Square of 5-square.js

const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (c) {
    let myStr = '';
    for (let i = 0; i < this.width; i++) {
      if (c === undefined) {
        myStr += 'X';
      } else {
        myStr += c;
      }
    }
    for (let j = 0; j < this.height; j++) {
      console.log(myStr);
    }
  }
}
module.exports = Square;
