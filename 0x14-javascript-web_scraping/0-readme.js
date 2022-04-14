#!/usr/bin/node
const fileSystem = require('fs');

fileSystem.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    throw (err);
  } else {
    console.log(data.toString());
  }
})