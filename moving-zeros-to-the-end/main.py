def move_zeros(lst):
    ''' this function moves all zeros to the end '''
    for each in lst:
        if each == 0:
            lst.remove(each)
            lst.append(each)
        else:
            pass
    
    return lst
