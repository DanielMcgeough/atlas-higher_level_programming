#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, respone) => {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ${response.statusCode}');
  }
});
