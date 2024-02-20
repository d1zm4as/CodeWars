def get_size(w,h,d):
    lista = [0,0]
    lista[0] = 2*(w*h) + 2*(w*d) +2*(h*d)
    lista[1] = w*h*d
    return lista