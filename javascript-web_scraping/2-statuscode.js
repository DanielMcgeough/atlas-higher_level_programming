#!/usr/bin/node

const { STATUS_CODES } = require('http');
const request = require('request');
const url = process.argv[2];

request.get(url, (error, respone) => {
    if (error) {
        console.log(error);
    } else {
        console.log('code: ${response.statusCode}');
    }
});
