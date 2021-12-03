const fs = require("fs");
const { verify } = require("../common.js");

const commands = fs.readFileSync("input.txt").toString().split("\n");

const getPosOffset = (commands) => {
  const offset = {
    aim: 0,
    y: 0,
    z: 0,
  };

  commands.forEach((command) => {
    const value = parseInt(command.split(" ")[1]);
    switch (command.split(" ")[0]) {
      case "forward":
        offset.y += value;
        offset.z += offset.aim * value;
        break;
      case "down":
        offset.aim += value;
        break;
      case "up":
        offset.aim -= value;
        break;
    }
  });

  return { y: offset.y, z: offset.z };
};

verify(
  getPosOffset,
  [["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]],
  { y: 15, z: 60 }
);

const pos = getPosOffset(commands);
console.log("Result: " + pos.y * pos.z);
