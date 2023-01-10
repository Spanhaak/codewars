def duplicate_encode(word):
    ''' this function changes the input to a specifc char if a char is more than 1 time in the string '''
    one     = '('
    more    = ')'

    # make the input lower-case for comparison
    word = word.lower()

    my_list = []
    
    # loop over the letter and count if they occure more than once, add wanted char to list
    for letter in word:
        counter = word.count(letter)
        if counter > 1:
            my_list.append(")")
        else:
            my_list.append("(")    

    # chang the list back into a string and return it
    my_string = ' '.join(my_list)
    my_string = my_string.replace(" ", "")

    return my_string