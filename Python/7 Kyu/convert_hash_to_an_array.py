def convert_hash_to_array(h):
    lista = []

    for x in h:
        print(x)
        lista.append([x,h[x]])

    return sorted([x for x in lista],key = lambda x : x[0])




# def convert_hash_to_array(hash):
#     return sorted(map(list, hash.items()))