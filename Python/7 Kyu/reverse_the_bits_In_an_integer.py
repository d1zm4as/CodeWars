def reverse_bits(n):
    a  = bin(n)[2:]
    
    return int(a[::-1],2)
