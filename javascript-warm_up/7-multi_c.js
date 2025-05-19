#!/usr/bin/node

let times = parseInt(process.argv[2])

if (!isNaN(times)) {
  if (times >= 1) {
    for (let i of Array(times).keys()) {
        console.log('C is fun');
    }
  }
} else {
  console.log('Missing number of occurrences');
}
