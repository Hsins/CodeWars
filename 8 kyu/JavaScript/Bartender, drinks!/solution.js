function getDrinkByProfession(param) {
  let bartender = param.toLowerCase();
  let drinkPair = {
    "jabroni": "Patron Tequila",
    "school counselor": "Anything with Alcohol",
    "programmer": "Hipster Craft Beer",
    "bike gang member": "Moonshine",
    "politician": "Your tax dollars",
    "rapper": "Cristal"
  }
  return drinkPair[bartender] ? drinkPair[bartender] : "Beer";
}