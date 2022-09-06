#!/usr/bin/node

const nbOccurences = (list, searchElement) => {
  let total = 0;
  list.forEach(
    (item) => {
      if (item === searchElement) {
        total = total + 1;
      }
    }
  );
  return total;
};
module.exports = { nbOccurences };
