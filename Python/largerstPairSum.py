def largest_pair_sum(numbers): 
    # your code here
    a  = sorted(numbers,reverse=True)
    return a[0]+a[1]