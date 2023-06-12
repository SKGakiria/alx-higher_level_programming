#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const numArgs = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((x, y) => x - y);
  console.log(numArgs[numArgs.length - 2]);
}
