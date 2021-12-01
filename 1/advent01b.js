const input = require("./input.json");
const { verify } = require("./common.js");
const { nbrLargerThanPrev } = require("./advent01a.js");

const slidingThreeSums = (values) =>
  values
    .map((v, i) => (i < 2 ? null : values[i] + values[i - 1] + values[i - 2]))
    .filter((v) => v !== null);

verify(slidingThreeSums, [1, 2, 3, 4, 5, 6], [6, 9, 12, 15]);

console.log(nbrLargerThanPrev(slidingThreeSums(input)));
