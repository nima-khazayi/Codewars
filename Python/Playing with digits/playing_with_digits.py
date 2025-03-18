def dig_pow(n, p):
    
    result = 0
    num = n
    digits = 0
    
    while (num > 0):
        num = num // 10
        digits += 1 # count digits
        
    num = n
    
    # set the power of each digit starting based on p in ascending order
    for i in range(1, digits + p):
        result += (num % 10)**(digits + p - i) 
        num = num // 10
        
    # check if the result would be equal to k*n or not
    k = result // n
    tmp = k * n
    
    # if k was integer then the result is true
    if (result == tmp):
        return k
        
    else:
        return -1
