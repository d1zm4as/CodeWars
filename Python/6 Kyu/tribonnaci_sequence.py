def tribonacci(sigs, n):
    cont= 0
    lim = n
    rep = n-len(sigs)
    seq = sigs
    if n==1:return [sigs[0]]
    if n<=0:return []
    if n< len(sigs):return sigs[:n]
    for _ in range(rep):
        soma = sum(seq[cont:lim])
        seq.append(soma)
        cont+=1
        lim+=1
    return seq
    

