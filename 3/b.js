const fs = require("fs");
const { verify } = require("../common.js");

const measurements = fs.readFileSync("input.txt").toString().split("\n");

const getValue = (input, selector) => {
  let candidates = input;

  let index = 0;
  while (candidates.length > 1) {
    const leastCommon = selector(candidates, index);

    candidates = candidates.filter((c) => c.charAt(index) === leastCommon);
    index++;
  }
  return candidates[0];
};

const mostCommonAtIndex = (input, i) =>
  input.map((word) => word.charAt(i)).filter((n) => n === "1").length >=
  input.length / 2
    ? "1"
    : "0";

const ogrSelector = (candidates, index) => mostCommonAtIndex(candidates, index);

const csrSelector = (candidates, index) =>
  mostCommonAtIndex(candidates, index) === "1" ? "0" : "1";

const testData = ["101", "111", "010", "110", "000"];
verify(getValue, [testData, ogrSelector], "111");
verify(getValue, [testData, csrSelector], "000");

console.log(
  "Result: " +
    parseInt(getValue(measurements, ogrSelector), 2) *
      parseInt(getValue(measurements, csrSelector), 2)
);
