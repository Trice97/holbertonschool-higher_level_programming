#!/usr/bin/node
const nbArgs = Process.argv.length - 2;

if (nbargs === 0) {
  console.log('No argument');
} else if (nbargs === 1) {
  console.log('Argument found');
} else {
  console.log('argumenrs found');
}
