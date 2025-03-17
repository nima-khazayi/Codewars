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
    # if it has only 1 digit return the number
    if (digits != 1):
        # otherwise we calculate sum of the number digits
        while (num1 > 0):
            for i in range(digits):
                sum += num1 % 10
                num1 = num1 // 10
        # call function to recalculate digital roots
        # passing the argument of sum as the summation 
        # of the last number digits
        return digital_root(sum)    

    else:
        return n
