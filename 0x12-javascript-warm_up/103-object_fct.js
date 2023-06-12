#!/usr/bin/node
// updates script by adding a new function incr that increments integer value

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.incr = function() {
  myObject.value++; 
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
