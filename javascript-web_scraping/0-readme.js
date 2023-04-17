#!/usr/bin/node

const fs = require('fs');

const filepath = process.argv[2];

fs.readFile(filepath, 'utf-8', function (err, data) {
  if (err) throw err;
  console.log(data);
});
