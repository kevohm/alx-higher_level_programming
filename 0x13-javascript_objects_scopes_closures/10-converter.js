#!/usr/bin/node
const converter = function (base) {
  return function (val) {
    return parseInt(val + '', 10).toString(base);
  };
};
module.exports = { converter };
