import math

def is_square(n):
    
    # not a perfect square if it's negative
    if (n < 0):
        return False
    
    # is a perfect square if it's 1 or 0
    elif (n == 1 or n == 0):
        return True
    
    else:
        mod = n % 10
        # a perfect square never ends up with 2, 3, 7 or 8
        if (mod == 2 or mod == 3 or mod == 7 or mod == 8):
            return False
        
        else:
          """
            there was also another method to check the digital roots
            the result should be a single digit number which is perfect square 
            but as we don't know how large are the entry numbers
            adding that method, might just increase the program complexity
          """
            sq = math.sqrt(n)
            sq = round(sq)
          """
            so we just check if the calculated root is an integer or not
            if it is, it should not make any difference to round it
            and if there was no difference the squared of it 
            should gives us the entry number 
          """
            if (sq ** 2 == n):
                return True
            
            else:
                return False
