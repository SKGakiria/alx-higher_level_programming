#!/usr/bin/node
// script that prints, if the first argument can be converted to an integer

const arg = process.argv[2];
if (isNaN(arg)) {
  console.log(`Not a number`);
} else {
  console.log('My number:', parseInt(arg));
}
