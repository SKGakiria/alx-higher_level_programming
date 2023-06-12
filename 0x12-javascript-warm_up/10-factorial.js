#!/usr/bin/node
// script that computes and prints a factorial

const value = parseInt(process.argv[2]);

function factorial (num) {
  if (num < 0) return;
  if (num === 0) return 1;
  return num * factorial(num - 1);
}

if (isNaN(value)) {
  console.log(1);
} else {
  console.log(factorial(value));
}
