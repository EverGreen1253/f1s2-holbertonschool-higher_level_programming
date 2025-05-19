#!/usr/bin/node

const times = parseInt(process.argv[2]);
let count = 0;

if (!isNaN(times)) {
  if (times >= 1) {
    while (count < times) {
      console.log('C is fun');
      count++;
    }
  }
} else {
  console.log('Missing number of occurrences');
}
