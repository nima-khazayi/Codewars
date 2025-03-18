def persistence(n, count=0):
    
    mul = 1
    digits = 0
    num = n   
    # counting digits
    while (num > 0):
        num = num // 10
        digits += 1
    # if number was not a single digit number
    # multiply digits to each other
    if (digits > 1):

        for _ in range(digits):
            mul *= n % 10
            n = n // 10
        # counting the times we use the function
        count += 1
        # recursively call the function
        return persistence(mul, count)
    
    # at the end the number should become a single digit 
    # in that case we return the defined counter for persistence running time
    else:
        return count
