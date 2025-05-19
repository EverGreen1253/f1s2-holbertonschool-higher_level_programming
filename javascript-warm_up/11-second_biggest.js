#!/usr/bin/node

let argList = [];
let largest = 0;
let secondLargest = 0;

if (process.argv.length <= 2) {
  console.log(0);
} else {
  argList = process.argv.slice(2);
  // console.log(argList)

  // Be careful, we're dealing with strings...
  for (const v of argList) {
    if (parseInt(v) > parseInt(largest)) {
      secondLargest = largest;
      largest = v;
    }
  }

  console.log(secondLargest);
}
