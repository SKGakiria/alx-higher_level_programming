#!/usr/bin/node
// a script that imports an array and computes a new array

const aList = require('./100-data').list;
console.log(aList);
const newList = aList.map((x, index) => x * index);
console.log(newList);
