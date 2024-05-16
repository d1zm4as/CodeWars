def swap_adjacent_bits(n):
    s = bin(n)[2:]
    s = s.zfill(32)
    size = 2
    a = "".join([s[i:i + size][::-1] for i in range(0, len(s), size)])
    return int(a,2)
    
    