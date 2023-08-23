def men_from_boys(arr):
    listae = []
    listai = []
    for x in set(arr):
        if x %2==0:
            listae.append(x)
        else:
            listai.append(x)
    listai = sorted(listai,reverse=True)
    listae = sorted(listae)
    return listae+listai