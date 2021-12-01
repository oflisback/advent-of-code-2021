const input = require("./input.json");
const { verify } = require("./common.js");

const nbrLargerThanPrev = (values) =>
  values.filter((v, i) => i > 0 && v > values[i - 1]).length;

if (!module.parent) {
  verify(nbrLargerThanPrev, [1, 2, 3], 2);
  verify(nbrLargerThanPrev, [3, 2, 1], 0);
  verify(nbrLargerThanPrev, [3, 2, 1, 2, 3], 2);

  console.log(nbrLargerThanPrev(input));
} else {
  exports.nbrLargerThanPrev = nbrLargerThanPrev;
}
