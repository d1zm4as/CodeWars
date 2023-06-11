def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    a = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    lista = int((sum([x*x for x in a])**0.5)/2)
    return lista