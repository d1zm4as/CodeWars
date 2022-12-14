def get_drink_by_profession(param):
    memo = {"jabroni":"Patron Tequila","school counselor":"Anything with Alcohol","programmer":"Hipster Craft Beer","bike gang member" :"Moonshine","politician" :"Your tax dollars","rapper":"Cristal"}
    return "Beer" if param.lower() not in memo else memo[param.lower()]
