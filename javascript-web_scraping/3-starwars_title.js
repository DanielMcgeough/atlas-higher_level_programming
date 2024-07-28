#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

const url = ('https://swapi-api.hbtn.io/api/films/');

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
