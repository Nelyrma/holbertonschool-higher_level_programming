#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  
  print () {
    for (let j = 0; j < this.height; j++) {
      let line = '';
      for (let i = 0; i < this.width; i++) {
        line += 'X';
      }
      console.log(line);
    }
  }

  rotate () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;   
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
