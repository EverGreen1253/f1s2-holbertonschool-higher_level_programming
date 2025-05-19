#!/usr/bin/node

// For some weird reason, semistandard wants a space between the 
// function name and the brackets
function add (a, b) {
  return a + b;
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  console.log(add(a, b));
}
