#!/usr/bin/node

let argList = [];
const intList = [];

if (process.argv.length <= 2) {
  console.log(0);
} else {
  argList = process.argv.slice(2);
  // console.log(argList)

  // Be careful, we're dealing with strings...
  for (const v of argList) {
    intList.push(parseInt(v));
  }

  intList.sort((a, b) => a - b).reverse();
  console.log(intList[1]);
}
