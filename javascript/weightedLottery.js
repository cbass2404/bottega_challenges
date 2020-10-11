// iterate over keys
// Object.keys
// bitwise

const weights = {
  winning: 1,
  losing: 500,
};

const weightedLottery = (w) => {
  let newArray = [];
  Object.keys(w).forEach((key) => {
    for (i = 0; i < w[key]; i++) {
      newArray.push(key);
    }
  });
  return newArray[(Math.random() * newArray.length) | 0];
};
//   return ((Math.random() * newArray.length) | 0) - 1;s
console.log(weightedLottery(weights));

while (true) {
  var count = 1;
  let result = weightedLottery(weights);
  if (result === "losing") {
    count = count + 1
    console.log(`Loser... Roll number ${count}`);
  } else {
    console.log(`Winner! Roll number ${count}`);
    return false;
  }
}
