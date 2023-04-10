#!/usr/bin/node
// script that prints x times "C is fun"

const sentence = 'C is fun';

const arg = process.argv.slice(2);

if (arg === 1) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < arg; i++) {
      console.log(sentence);
  }
} 