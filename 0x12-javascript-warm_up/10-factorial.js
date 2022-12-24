#!/usr/bin/node
function factorial (g) {
  if ((isNaN(g)) || (g === 1)) {
    return 1;
  } else {
    return factorial(g - 1) * g;
  }
}

console.log(factorial(parseInt(process.argv[2])));
