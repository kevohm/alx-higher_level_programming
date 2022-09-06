#!/usr/bin/node
const logMe = function (item) {
  let counter = 0;
  function print (item) {
    const ans = counter + ': ' + item;
    console.log(ans);
    return counter += 1;
  }
  return print(item);
};
module.exports = { logMe };
