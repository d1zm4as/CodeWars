def vowel_indices(word):
    lista = []
    for idx,x in enumerate(word):
        if x in "aeioYuAEyIOU":
            lista.append(idx+1)

    # lista = [x+1 for x in range(1,len(word))if word[x] in "aeiou"] 
    return lista
