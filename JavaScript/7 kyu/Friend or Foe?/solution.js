function friend(friends){
  // your code here
  return friends.filter(function(friend) {
    return friend.length === 4;
  })
}