String.prototype.toJadenCase = function () {
  let words = this.split(" ").map(function(word) {
    return word.charAt(0).toUpperCase() + word.slice(1);
  })
  return words.join(" ");
};