const prettyPrice = (price) => {
  if (price >= 1) {
    return (price | 0) + 0.95;
  } else if (price > .95) {
      return 1.95;
  } else if (typeof(price) === Number){
      return .95;
  } else {
      return `${price} is not a valid entry.`
  }
};

console.log(prettyPrice(3.05));
console.log(prettyPrice(1));
console.log(prettyPrice(.96));
console.log(prettyPrice('a'));
