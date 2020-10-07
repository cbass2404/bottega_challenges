const manExponent = (base, power) => {
  let total = 1;
  for (let i = 0; i < power; i++) {
    total *= base;
  }
  return total;
};

console.log(manExponent(4, 4));

// Jordans solution

const toThePowerOf = (num, exp) => {
  const items = Array(exp).fill(num);
  const reducer = (total, currentValue) => total * currentValue;
  return items.reduce(reducer);
};

console.log(toThePowerOf(2, 3));
