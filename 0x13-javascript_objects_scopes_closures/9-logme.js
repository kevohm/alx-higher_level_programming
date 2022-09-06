#!/usr/bin/node
let counter = 0;
const logMe = function (item) {
  function print (item) {
    const ans = counter + ': ' + item;
    console.log(ans);
    counter += 1;
  }
  return print(item);
};
module.exports = { logMe };
