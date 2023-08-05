def validate_hello(g):
    lista = ["hello","ciao","salut","hallo","hola","ahoj","czesc"]
    for x in lista:
        if x in g.lower():
            return True
    return False
