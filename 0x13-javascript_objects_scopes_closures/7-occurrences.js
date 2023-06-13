#!/usr/bin/node
// function that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let Ocount = 0;
  let i = 0;
  for (i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      Ocount += 1;
    }
  }
  return Ocount;
};
