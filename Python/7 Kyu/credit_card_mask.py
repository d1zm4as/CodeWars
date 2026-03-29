# return masked string
def maskify(cc):
    tam  = len(cc)
    if tam<=4:
        return cc
    
    return (tam-4)*"#"+cc[-4:]