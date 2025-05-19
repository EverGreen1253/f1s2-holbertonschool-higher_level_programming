#!/usr/bin/node

const size = parseInt(process.argv[2]);
let row = 0;
let col = 0;

if (!isNaN(size)) {
  if (size >= 1) {
    while (row < size) {
      col = 0;

      while (col < size) {
        process.stdout.write('X');
        col++;
      }

      console.log('');
      row++;
    }
  }
} else {
  console.log('Missing size');
}
