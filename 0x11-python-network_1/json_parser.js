#!/usr/bin/node
const fs = require('fs');
const file = fs.readFileSync(process.argv[1]);
console.log(JSON.stringify(JSON.parse(file.toString())));
