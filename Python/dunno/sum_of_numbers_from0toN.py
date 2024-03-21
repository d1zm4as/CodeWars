def show_sequence(n):
    if n ==0:
        return "0=0"
    if n <0:
        return f"{n}<0"
    a = ""
    soma = 0
    for x in range(n):
        a += f"{x}+"
        soma +=x
    a+=f"{n} = {soma+n}"
    return a
