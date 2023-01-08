def move_zeros(lst):
    ''' this function is to change the order in the list in such a way that number go last but the order of the others are unaffected'''

    zeros_at_end = lst

    for selected_number in lst:
        if selected_number is 0:
            zeros_at_end.remove(selected_number)
            zeros_at_end.append(selected_number)
        else:
            pass    

    return zeros_at_end
