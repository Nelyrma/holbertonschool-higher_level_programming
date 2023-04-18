#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (errr, response, body) => {
  if (error) {
    console.log(error);
      return;
  }

  const todos = JSON.parse(body);
  const completed = {};
  todos.forEach((todo) => {
    if (todo.completed && completed[todo.userId] === undefined) {
      completed[todo.userId] = 1;
    } else if (todo.completed) {
        completed[todo.userId] += 1;
    }
  });
  console.log(completed);
});
