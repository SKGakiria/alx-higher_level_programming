#!/usr/bin/node
// a class Rectangle that defines a rectangle

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let myStr = '';
    for (let i = 0; i < this.width; i++) {
      myStr += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(myStr);
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
