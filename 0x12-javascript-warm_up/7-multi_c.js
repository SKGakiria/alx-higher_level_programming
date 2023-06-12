#!/usr/bin/node
// script that prints x times “C is fun”

const args = process.argv[2];
if (isNaN(args)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(args); i++) {
    console.log('C is fun');
  }
}
