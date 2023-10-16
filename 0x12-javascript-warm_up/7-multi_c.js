#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const a = Number(process.argv[2]);
  for (let ctr = 0; ctr < a; ctr++) {
    console.log('C is fun');
  }
}
