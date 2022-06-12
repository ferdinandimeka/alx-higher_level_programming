#!/usr/bin/node

const fileSystem = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fileSystem.createWriteStream(process.argv[3]));