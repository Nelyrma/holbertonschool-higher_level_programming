#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/:id' + movieId

request(url, function (err, response, body) {
  console.log(JSON.parse(body).title || err);
});