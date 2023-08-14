from statistics import Counter

a = "CBAABC" 
a  = "RAMBUNCTIOUSLY"
a = "ABCBACCBA"
b = "DEFFED"
b = "THERMODYNAMICS"
b = "ABCBACCAB"
ca = Counter(a)
cb = Counter(b)

lista = [ca[x] for x in a]
listb = [cb[x] for x in b]

print(lista)
print(listb)

