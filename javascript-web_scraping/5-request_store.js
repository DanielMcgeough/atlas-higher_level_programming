#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const file = process.argv[3];
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file, body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
