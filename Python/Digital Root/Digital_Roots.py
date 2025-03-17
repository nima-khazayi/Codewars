def digital_root(n):
    # ...
    digits = 0 
    sum = 0
    num1 = n
    # counting initial number digits
    while (num1 > 0):   
        num1 = num1 // 10
        digits += 1
          
    num1 = n
    check = n // 10
    # if it has only 1 digit return the number
    if (check > 0):
        # otherwise we calculate sum of the number digits
        while (num1 > 0):
            for i in range(digits):
                sum += num1 % 10
                num1 = num1 // 10
            # set digits zero to count it for the result number    
            digits = 0
            
            # saving the sum that if in the below while we noticed that 
            # result has one digit we should return that
            sum1 = sum
            
            while (sum > 0):
                sum = sum // 10
                digits += 1
                
            # otherwise calculated summation is being set as the new number
            num1 = sum1
            
            if (digits == 1):
                break

        return num1
            
    else:
        return n
        
