memo = {"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine","10":"onezero","11":"oneone","12":"onetwo","13":"onethree","14":"onefour","15":"onefive"}




n = 999
n = 37 
n = 73
n  = 60
n = 311

def numbers_of_letters(n):
    a  = str(n)
    lista = []
    copy = "".join([memo[x] for x in a])
    if copy == "four":
        return [copy]
    lista.append(copy)
    
    tam = str(len(copy))
    while memo[tam]!='four':
        ref = memo[tam]
        lista.append(ref)
        tam = str(len(ref))


    lista.append('four')
    return lista