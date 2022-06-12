#!/usr/bin/node

const fileSystem = require('fs');
const file = process.argv[2];
const content = process.argv[3];
fileSystem.writeFile(file, content, 'utf-8', function (err) {
  if (err) {
    throw (err);
  }
});
