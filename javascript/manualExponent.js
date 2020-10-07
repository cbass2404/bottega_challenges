const manExponent = (base, power) => {
  let total = 1;
  for (let i = 0; i < power; i++) {
    total *= base;
  }
  return total;
};

console.log(manExponent(4, 4));
