def find_words(sentence, count, tmp, result):

    """
        in here the find_words function we if the count was more equal to 5 or not.
        if it was then we reverse first(count) characters if the string sentence
        and add it to reversed_temporary to get added in the result string.
        and if it was not then we just add it to the result.

        in here we also check if there is any other word in the string or not,
        by checking if there is any " " left, if there was we cut the first(count)
        characters from the string sentence and pass it to the spin_word function
        with the recent results and an empty space in between the words,
        and if there was not any words left, we just return the result.
    """
    
    temporary = tmp
    reversed_temporary = ""
    if (count >= 5):
        for i in range(count):
            reversed_temporary += sentence[count - (i+1)]

        result += reversed_temporary

    else:  
        result += temporary
    
    if (" " not in sentence):
        return result

    else:
        return spin_words(sentence[count+1:], result+" ")
    
def spin_words(sentence, result=""):

    """
        in this function we first check if we have a single word or a sentence,
        this could be different as we count the characters of the whole string
        or until we reach " " for the next word, we take the word in tmp
        and number of its chars in count then pass the arguments to the function find words.
    """
    
    count = 0
    i = 0
    tmp = ""
    
    if (" " not in sentence):
        while (i < len(sentence)):
            count += 1
            tmp += sentence[i]
            i += 1
        return find_words(sentence, count, tmp, result)

    else:
        while (sentence[i] != " "):
            count += 1
            tmp += sentence[i]
            i += 1 
        return find_words(sentence, count, tmp, result)
