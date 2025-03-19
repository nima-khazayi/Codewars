def pig_it(text):
    
    """
        and someday i will add comments to this code
    """
    
    if (" " not in text):
        text = text[1:] + text[0] + "ay"
        
        return text
    
    else:    
        res = ""
        i = 0
        c = 0

        while (i < len(text)):
            tmp = "" 
            
            while (text[c] != " "):

                if  c+1 == len(text):
                    tmp += text[c]
                    break

                else:
                    tmp += text[c]
                    c += 1

            c += 1
            i = c

            if tmp.isalpha():

                if i == len(text):
                    res += tmp[1:] + tmp[0] + "ay"
                
                else:
                    res += tmp[1:] + tmp[0] + "ay "
            
            else:

                if i == len(text):
                    res += tmp[1:] + tmp[0] 
                
                else:
                    res += tmp[1:] + tmp[0] + " "
                
        return res
