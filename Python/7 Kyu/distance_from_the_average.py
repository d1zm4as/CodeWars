def distances_from_average(test_list):
    soma = sum(test_list)
    tam = len(test_list)
    
    avg  = soma/tam
    
    return [round(avg-x,2) for x in test_list]