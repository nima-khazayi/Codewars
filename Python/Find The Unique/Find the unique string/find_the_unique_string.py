def find_uniq(arr):
    
    new_arr = []
    
    # as the set function is case sensitive convert all elements to lowercase
    for i in range(len(arr)):
        new_arr.append(str(arr[i]).lower())
    
    # to prevent multiple same char sensitivity
    for i in range(len(new_arr)):
        new_arr[i] = set(new_arr[i])
    
    # find the unique element and return it as it was from arr list
    if new_arr[0] == new_arr[1]:

        for i in range(2, len(new_arr)):
            if new_arr[0] != new_arr[i]:
                return arr[i]
            
    elif new_arr[0] == new_arr[2]:
        return arr[1]
    
    else:
        return arr[0]
        
