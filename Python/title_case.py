# a = 'a clash of KINGS' 
# b = 'a an the of'

# res  = 'A Clash of Kings'

# a = 'THE WIND IN THE WILLOWS' 
# b = 'The In'

# res =  'The Wind in the Willows'
        
        
a = 'the quick brown fox'
b = '' 

res = 'The Quick Brown Fox'


lista= a.split()

copy = []
copy.append(lista[0].capitalize())
for x in lista[1:]:
    if x.lower() in b.lower():
        print("oiue")
        copy.append(x.lower())             
    else:
        copy.append(x.capitalize())


print(" ".join(copy))
print(" ".join(copy)==res)