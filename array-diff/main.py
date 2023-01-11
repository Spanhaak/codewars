def array_diff(a, b):
    ''' This function returns a list but removes the items of the second list '''
    print(f'list a: ', a)
    print(f'list b: ', b)
    for each_b in b:
        amount_in_a = a.count(each_b)
        print(f'Total amount in List a: ', amount_in_a)
        while amount_in_a != 0:
            if each_b in a:
                a.remove(each_b)
                amount_in_a = amount_in_a - 1    
    print(f'Current list is: ', a)
    return a
