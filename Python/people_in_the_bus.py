

def number(bus_stops):
    total = 0
    for x in bus_stops:
        a = x[0]
        b = x[1]
        total += (a-b)
    return total
    

