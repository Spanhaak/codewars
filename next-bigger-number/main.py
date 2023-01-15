''' WIP '''
def next_bigger(n):
    ''' function that takes an positive integer and returns the next bigger number '''
    n = str(n)
    my_list = []

    for each in n:
        each = int(each)
        my_list.append(each)
    
    print(f"The list:",my_list)

    if len(my_list) < 2:
        print(-1)
        return -1

    length = len(my_list)
    print(f"Length of the list:",length)
    
    # print(my_list[length-2])

    if my_list[1] > my_list[0]:
        result = str(my_list[0]) + str(my_list[1])
        result = ''.join(result)
        print(result)
        return result
    if my_list[1] == my_list[0]:
        print(-1)
        return -1
    if my_list[1] < my_list[0]:
        print(-1)
        return -1    






next_bigger(1)