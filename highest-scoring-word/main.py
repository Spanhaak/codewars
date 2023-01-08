def high(x):
    '''a function to get the highest scoring word, where the letters in the word are translated to the alphabetical number '''
    
    # split the list, make an empty dict for later sorting 
    wordlist = x.split()
    my_dict = {}
    which_word = 0

    # loop through the list and convert the letters of each word to numbers and add them up
    for word in wordlist:
        which_word = which_word + 1
        total_word = 0
        for char in word:
            number = ord(char)-96
            total_word = total_word + number
        my_dict[word] = total_word
    print(f"The unsorted dict is:", my_dict)
    
    # sort the dict
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True ))
    print(f"The sorted dict is:",sorted_dict)
    
    # return the result of the highest word
    result = list(sorted_dict.keys())[0]
    
    return result

high('man i need a taxi up to ubud')