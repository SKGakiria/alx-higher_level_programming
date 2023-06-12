#!/usr/bin/node
// script that prints a square

const size = parseInt(process.argv[2]);
let column = '';

if (isNaN(size)) {
  console.log("Missing size");
} else {
  for (let i = 0; i < size; i++) {
    column += "X";
  }

  for (let j = 0; j < size; j++) {
    console.log(column);
  }
}
