#!/usr/bin/node

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

function add (a, b) {
  if (!isNaN(a) && !isNaN(b)) {
    const sum = a + b;
    console.log(sum);
  } else {
    console.log('NaN');
  }
}
add(a, b);
