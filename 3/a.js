const fs = require("fs");
const { verify } = require("../common.js");

const measurements = fs.readFileSync("input.txt").toString().split("\n");

const mostCommonBit = (input, i) =>
  input.map((word) => word.charAt(i)).filter((n) => n === "1").length >
  input.length / 2
    ? "1"
    : "0";

const testData = ["101", "111", "010", "110", "110"];
verify(mostCommonBit, [testData, 0], "1");
verify(mostCommonBit, [testData, 1], "1");
verify(mostCommonBit, [testData, 2], "0");

const gamma = [...Array(measurements[0].length).keys()]
  .map((i) => mostCommonBit(measurements, i))
  .join("");
const epsilon = [...gamma].map((c) => (c === "1" ? "0" : "1")).join("");

console.log("Result: " + parseInt(gamma, 2) * parseInt(epsilon, 2));
