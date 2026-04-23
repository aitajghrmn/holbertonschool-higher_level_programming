#!/usr/bin/node

const input = parseInt(process.argv[2], 10);

function factorial (n) {
  if (isNaN(n) || n === 0 || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(input));
