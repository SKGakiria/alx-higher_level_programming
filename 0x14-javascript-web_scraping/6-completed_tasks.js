#!/usr/bin/node
// script computes the number of tasks completed by user id

const request = require('request');
const apiURL = process.argv[2];

request.get(apiURL, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const tasksCompleted = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!tasksCompleted[todo.userID]) {
        tasksCompleted[todo.userID] = 1;
      } else {
        tasksCompleted[todo.userID] += 1;
      }
    }
  });
  console.log(tasksCompleted);
});
