#!/usr/bin/node
import { argv } from 'process';

//a script that prints a message depending of the number of arguments passed
if (argv.length == 0) {
  console.log('No argument');
}
else {
  console.log('Argument found');
};

