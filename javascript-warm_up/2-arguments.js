#!/usr/bin/node

/*
console.log(process.argv) will print out an array
For example:

./2-arguments.js Best School
[
  '/usr/bin/node',
  '/home/Work/Holberton/f1s2-holbertonschool-higher_level_programming/javascript-warm_up/2-arguments.js',
  'Best',
  'School'
]
*/

if (process.argv.length <= 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else { // 3 or more
  console.log('Arguments found');
}
