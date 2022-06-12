#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];
request.get(url + id, function (err, response, body) {
  if (err) {
    throw (err);
  } else {
    console.log(JSON.parse(body).title);
  }
})