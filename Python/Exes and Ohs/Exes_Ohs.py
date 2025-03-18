def xo(s):

    x = 0
    o = 0
    
    # linear search used to count each lower/upper case Xs and Os
    for i in range(len(s)):

        if (s[i] == "x" or s[i] == "X"):
            x += 1
            
        elif (s[i] == "o" or s[i] == "O"):
            o += 1

    if (x == o):
        return True
    
    else:
        return False
