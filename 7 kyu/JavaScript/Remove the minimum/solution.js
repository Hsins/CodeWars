function removeSmallest(numbers) {
  let removedArray = numbers.slice();
  let pos = numbers.indexOf(Math.min(...numbers));
  removedArray.splice(pos, 1);
  return removedArray;
}