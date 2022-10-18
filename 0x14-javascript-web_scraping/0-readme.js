#!/bin/node
const { readFileSync } = require('fs');
const content = readFileSync(process.argv[2], 'utf-8');
console.log(content);
