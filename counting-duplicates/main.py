def duplicate_count(text):
    '''this function is to count duplicates of distinct case-insensitive alphabetic chars and numeric digits'''
    
    # first make sure the list is lower case to ease up comparison
    lower_case_list = text.lower()

    my_list = []

    # start a counter to help the counting process
    for item in set(lower_case_list):
        counts = lower_case_list.count(item)
        # apply the counts to the empty list if the counts are higher than 1
        if counts >= 2:
            my_list.append(counts)
    return len(my_list)
