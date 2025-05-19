#!/usr/bin/node

if (!process.argv[2]) {
  console.log('No argument');
}

for (const index in process.argv) {
  if (index === '2') {
    console.log(process.argv[index]);
  }
}
