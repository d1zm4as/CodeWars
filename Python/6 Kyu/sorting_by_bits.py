
def cont(n):
    return bin(n)[2:].count("1"),n

def sort_by_bit(lista): 
    lista.sort(key = cont)
    return lista