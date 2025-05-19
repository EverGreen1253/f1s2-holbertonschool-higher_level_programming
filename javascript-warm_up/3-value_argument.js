#!/usr/bin/node

for (index in process.argv) {
  if (index == 2) {
    console.log(process.argv[index]);
  }
}
