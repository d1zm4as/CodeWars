from statistics import Counter

t = 'cedewaraaossoqqyt' 
t = 'rkqodlw'
t = "scriptingjava"
t = "katas"
t = "cedewaraaossoqqyt"

s = 'world'
s = 'codewars'
s = "javascript"
s = "steak"
s = 'codewars'


a = Counter(t)

b =Counter(s)

lista = []
for x in s:
    if b[x]<=a[x]:
        lista.append(x)
print(len(lista)==len(s))