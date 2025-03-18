def solution(s):
    
    string = []
    
    # condition for even number of characters in string    
    if (len(s) % 2 == 0):
    
        for i in range(0, len(s), 2):
            str = s[i] + s[i+1] # add chars to each other 2 by 2
            string.append(str) # add them to the final list
    
        return string
        
    # condition for odd number of characters in string
    else:
        
        for i in range(0, len(s) - 1, 2):
            str = s[i] + s[i+1] # add chars to each other 2 by 2
            string.append(str) # add them to the final list
            
        str = s[-1] + "_" # for the last char, add "_" 
        string.append(str) # add it to the final list
        
        return string
