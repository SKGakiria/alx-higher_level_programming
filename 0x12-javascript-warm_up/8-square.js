#!/usr/bin/node
// script that prints a square

const size = parseInt(process.argv[2]);
let row = '';

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    row += 'X';
  }

  for (let j = 0; j < size; j++) {
    console.log(row);
  }
}
