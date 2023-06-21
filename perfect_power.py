def solve(n):
    
    x, y = 2, 2
    while x**2 <= n:
        if x**y == n:
            return[x,y]
        if x**y > n:
            x+=1
            y = 1
        y+=1        
    return None

pp = [4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144, 169, 196, 216, 225, 243, 256, 289, 324, 343, 361, 400, 441, 484]

lista = [solve(x) for x in pp]

print(lista)