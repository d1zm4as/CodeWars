a = 'sTreSS'
s = a.lower()
for x in s:
    if s.count(x)==1:
        idx= s.index(x)
        print(a[idx])
        break
 


