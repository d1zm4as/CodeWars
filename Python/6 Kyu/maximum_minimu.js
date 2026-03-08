function max() {
  const arr = [...arguments].toString().split(",").map(Number);
  const nan = arr.some((el) => Number.isNaN(el));
  if (!nan) {
    arr.sort((a, b) => b - a);
    return arr[0];
  }
  return NaN;
}

function min() {
  const arr = [...arguments].toString().split(",").map(Number);
  const nan = arr.some((el) => Number.isNaN(el));
  if (!nan) {
    arr.sort((a, b) => a - b);
    return arr[0];
  }
  return NaN;
}