def unique_sum(lst):
    
    sum = 0
    newlist = list(set(lst))
    if len(newlist) == 0:
        return None
    
    for i in range(len(newlist)):
        sum += newlist[i]
    
    return sum
