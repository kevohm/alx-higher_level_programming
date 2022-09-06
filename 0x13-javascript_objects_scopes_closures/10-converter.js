#!/usr/bin/node
const converter = function (base) {
  return function (num) { return parseInt(num, base); };
};
module.exports = { converter };
