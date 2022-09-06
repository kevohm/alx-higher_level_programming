#!/usr/bin/node
const converter = function (base) {
  return function (num) { return parseInt(num + '', 10).toString(base); };
};
module.exports = { converter };
