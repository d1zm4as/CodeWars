def correct_polish_letters(s): 
    memo  = {"ą" : "a",
"ć" : "c",
"ę" : "e",
"ł" : "l",
"ń" : "n",
"ó" : "o",
"ś" : "s",
"ź" : "z",
"ż" : "z"}
    
    copy = ""
    for x in s:
        if x in memo:
            copy+=memo[x]
        else:
            copy+=x
    return copy