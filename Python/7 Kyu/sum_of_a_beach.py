def sum_of_a_beach(s):
    # your code
    s = s.lower()
    
    return s.count("sand")+s.count("water")+ s.count("fish")+s.count('sun')