#!/usr/bin/node
// function prints the no of arguments already printed and the new arg value

let aCount = 0;
exports.logMe = function (item) {
  console.log(`${aCount++}: ${item}`);
};
