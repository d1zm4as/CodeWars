def hex_hash(code):
    soma = 0
    for x in code:
        soma+=sum([int(y) for y in hex(ord(x)) if y.isdigit()]) 
    return soma