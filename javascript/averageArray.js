let numList = []

const avgList = list => list.reduce((a, b) => a + b, 0) / list.length

console.log(avgList(numList))