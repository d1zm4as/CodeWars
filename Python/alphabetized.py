def alphabetized(s):

#     lista = sorted([x for x in s if x.isalpha()],key=str.lower)
    
#     return "".join(lista)
# usar o filter inves do list conprehension
    return "".join(sorted(filter(str.isalpha, s),key=str.lower))