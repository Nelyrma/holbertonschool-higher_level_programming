#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const films = JSON.parse(body).results;

  let countFilm = 0;
  for (const film of films) {
    for (const character of film.characters) {
      if (character.includes('18')) {
        countFilm++;
        break;
      }
    }
  }
  console.log(countFilm);
});
