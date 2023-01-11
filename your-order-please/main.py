import re
def order(sentence):
    ''' This function puts the words in the right order '''

    my_dict = {}
    splitted = sentence.split()

    # build the dict based on the amount of words
    for each_word in splitted:
        found_number = re.findall(r'\d+', each_word)
        found_number = found_number[0]
        my_dict[found_number] = each_word
    print(my_dict)

    # sort the dict keys so the order is correct
    myKeys = list(my_dict.keys())
    myKeys.sort()
    sorted_dict = {i: my_dict[i] for i in myKeys}
   
    # return the dict values in order as a string
    new_order_string = (' '.join(['{1}'.format(k, v) for k,v in sorted_dict.items()]))

    # this has nothing to do with the band
    return new_order_string
    