class arrayPopper {
  constructor(a) {
    this.a = a;
  }

  shiftPop() {
    if (this.a.length >= 1) {
      return this.a.length % 2 == 0 ? this.a.shift() : this.a.pop();
    } else {
      return "Array is Empty";
    }
  }
}

const arrayList = new arrayPopper([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]);

console.log(arrayList.shiftPop());
console.log(arrayList.shiftPop());
console.log(arrayList.shiftPop());
console.log(arrayList.shiftPop());
console.log(arrayList.shiftPop());
console.log(arrayList.shiftPop());
console.log(arrayList.shiftPop());
console.log(arrayList.shiftPop());
console.log(arrayList.shiftPop());
console.log(arrayList.shiftPop());
console.log(arrayList.shiftPop());
