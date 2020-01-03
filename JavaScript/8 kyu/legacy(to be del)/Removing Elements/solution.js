function removeEveryOther(arr){
  // your code here
  return arr.filter(function(item, index) {
    return (index % 2 === 0);
  });
}