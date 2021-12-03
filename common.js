exports.verify = (func, input, expectation) => {
  if (JSON.stringify(func(...input)) === JSON.stringify(expectation)) {
    console.log("Pass!");
  } else {
    console.log("Fail!");
  }
};
