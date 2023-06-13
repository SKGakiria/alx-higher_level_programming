#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {
  const rlistCopy = [];
  let i = 0;
  for (i = list.length - 1; i >= 0; i--) {
    rlistCopy.push(list[i]);
  }
  return (rlistCopy);
};
