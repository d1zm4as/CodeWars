def even_numbers(arr,n):
    lista = [x for x in arr if x %2==0]
    return lista[len(lista)-n::]
