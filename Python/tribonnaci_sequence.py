seq = [1, 1, 1]

n = 10

#for _ in range(10)
#lista  = [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
cont = 0
lim = 3
rep = n-len(seq)
for _ in range(rep):
    soma = sum(seq[cont:lim])
    seq.append(soma)
    print(seq)
    cont+=1
    lim+=1
    

