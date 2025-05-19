#!/usr/bin/node

if (!process.argv[2]) {
  process.stdout.write('undefined');
} else {
  process.stdout.write(process.argv[2]);
}

process.stdout.write(' is ');

if (!process.argv[3]) {
  console.log('undefined');
} else {
  console.log(process.argv[3]);
}
