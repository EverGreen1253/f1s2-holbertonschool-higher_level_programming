#!/usr/bin/node

function factorial (n) {
  let result = 1;

  if (n < 0) {
    result = -1;
  }

  if (n === 0) {
    result = 1;
  }

  if (n > 0) {
    result = (n * factorial(n - 1));
  }

  return (result);
}

const arg = parseInt(process.argv[2]);
const factor = isNaN(arg) ? 1 : arg;

console.log(factorial(factor));
