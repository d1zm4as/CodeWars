word = 'supercalifragilisticexpialidocious'
word = 'apple'
res = [2, 4, 7, 9, 12, 14, 16, 19, 21, 24, 25, 27, 29, 31, 32, 33]
res  = [1,5]
lista = []


for idx,x in enumerate(word):

    print(x,idx)
    if x in "aeiou":
        lista.append(idx+1)

# lista = [x+1 for x in range(1,len(word))if word[x] in "aeiou"] 
print(lista)
print(lista==res)