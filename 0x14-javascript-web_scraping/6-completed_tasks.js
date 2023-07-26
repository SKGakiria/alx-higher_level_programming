#!/usr/bin/node
// script computes the number of tasks completed by user id

const request = require('request');
const apiURL = process.argv[2];

request.get(apiURL, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const tasksCompleted = {};
    body.forEach((todo) => {
      if (todo.completed) {
        if (todo.userId in tasksCompleted) {
          tasksCompleted[todo.userId] += 1;
        } else {
          tasksCompleted[todo.userId] = 1;
        }
      }
    });
    console.log(tasksCompleted);
  }
});
