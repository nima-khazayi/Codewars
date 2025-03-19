def find_uniq(arr):
    
    a, b = set(arr)
    
    if arr.count(a) == 1:
        return a
    
    else:
        return b
