def find_it(seq):
    ''' This function returns the odd integer '''
    my_dict = {}
    for number in seq:
        if number in my_dict:
            my_dict[number] = my_dict[number] + 1
        else:
            my_dict[number] = 1
    for k, v in my_dict.items():
        if (v % 2) == 1: 
            return k
