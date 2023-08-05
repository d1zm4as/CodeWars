def encode(st): #change to #h2ll4
    """memo = {"a":"1","e":"2","i":"3","o":"4","u":"5"}
    lista = []
    for x in st:
        if x in memo:
           lista.append(memo[x])
        else:
            lista.append(x) """
    #return "".join([lista])
    return st.replace("a","1").replace("e","2").replace("i","3").replace("o","4").replace("u","5")
def decode(st): #change back to normal
    """memo = {"1":"a","2":"e","3":"i","4":"o","5":"u"}
    lista = []
    for x in st:
        if x in memo:
            lista.append(memo[x])
        else:
            lista.append(x)
    return "".join(lista)
"""
    return st.replace("1","a").replace("2","e").replace("3","i").replace("4","o").replace("5","u")
    
memo = {"a":1,"e":2,"i":3,"o":4,"u":5}

st = 'hello' #h2ll4

for x in memo:
    print(x,memo[x])


print(encode(st))

print(decode(encode(st)))