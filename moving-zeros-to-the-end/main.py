def move_zeros(lst):
    zeros_at_end = lst
    print(lst)
    print(zeros_at_end)
    for selected_number in lst:
        if selected_number is 0:
            zeros_at_end.remove(selected_number)
            zeros_at_end.append(selected_number)
            print(zeros_at_end)
        else:
            pass    
    print (zeros_at_end)
    
    
    
    
    
    # return lst


move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])