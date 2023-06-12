#!/usr/bin/node
// script that prints, if the first argument can be converted to an integer

const arg = process.argv[2];
const num = Number(arg);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(arg));
}
