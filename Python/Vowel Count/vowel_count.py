def get_count(sentence):

    vowels = 0
    
    # linear search for vowels in the sentence
    for i in range(len(sentence)):
        if (sentence[i] == "a" or sentence[i] == "e" or sentence[i] == "i"
            or sentence[i] == "u" or sentence[i] == "o"):
            vowels += 1

    return vowels
